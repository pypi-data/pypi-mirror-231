"""
Module for running photometric calibration
"""
import logging
import warnings
from collections.abc import Callable
from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.io.fits.verify import VerifyWarning
from astropy.stats import sigma_clip, sigma_clipped_stats
from astropy.table import Table

from mirar.catalog.base_catalog import BaseCatalog
from mirar.data import Image, ImageBatch
from mirar.errors import ProcessorError
from mirar.paths import MAGLIM_KEY, ZP_KEY, ZP_NSTARS_KEY, ZP_STD_KEY, get_output_dir
from mirar.processors.astromatic.sextractor.sextractor import sextractor_checkimg_map
from mirar.processors.astrometry.validate import get_fwhm
from mirar.processors.base_catalog_xmatch_processor import (
    BaseProcessorWithCrossMatch,
    default_image_sextractor_catalog_purifier,
)

logger = logging.getLogger(__name__)

# All the Sextractor parameters required for this script to run
REQUIRED_PARAMETERS = [
    "X_IMAGE",
    "Y_IMAGE",
    "FWHM_WORLD",
    "FLAGS",
    "ALPHAWIN_J2000",
    "DELTAWIN_J2000",
    "MAG_APER",
    "MAG_AUTO",
]


class PhotometryError(ProcessorError):
    """Base error for photometric calibration"""


class PhotometryReferenceError(PhotometryError):
    """Error related to the photometric reference catalogue"""


class PhotometrySourceError(PhotometryError):
    """Error related to the photometric source catalogue"""


class PhotometryCrossMatchError(PhotometryError):
    """Error related to cross-matching photometric reference and source catalogues"""


class PhotometryCalculationError(PhotometryError):
    """Error related to the photometric calibration"""


def get_maglim(
    bkg_rms_image_path: str | Path,
    zeropoint: float | list[float],
    aperture_radius_pixels: float | list[float],
) -> float:
    """
    Function to calculate limiting magnitude
    Args:
        bkg_rms_image_path:
        zeropoint:
        aperture_radius_pixels:
    Returns:
    """
    if isinstance(zeropoint, float):
        zeropoint = [zeropoint]
    if isinstance(aperture_radius_pixels, float):
        aperture_radius_pixels = [aperture_radius_pixels]

    zeropoint = np.array(zeropoint, dtype=float)
    aperture_radius_pixels = np.array(aperture_radius_pixels, dtype=float)
    logger.debug(aperture_radius_pixels)
    bkg_rms_image = fits.getdata(bkg_rms_image_path)
    bkg_rms_med = np.nanmedian(bkg_rms_image)
    noise = bkg_rms_med * np.sqrt(np.pi * aperture_radius_pixels**2)
    maglim = -2.5 * np.log10(5 * noise) + zeropoint
    logger.debug(f"Aperture radii: {aperture_radius_pixels}")
    logger.debug(f"Calculated maglim: {maglim}")
    return maglim


class PhotCalibrator(BaseProcessorWithCrossMatch):
    """
    Photometric calibrator processor

    Attributes:
        num_matches_threshold: minimum number of matches required for
        photometric calibration
        outlier_rejection_threshold: float or list of floats to use as number of sigmas
        for outlier rejection. If a ist is provided, the list is sorted and stepped
        through in order with increasing thresholds until the specified
        number of matches is reached.
    """

    base_key = "photcalibrator"

    def __init__(
        self,
        ref_catalog_generator: Callable[[Image], BaseCatalog],
        temp_output_sub_dir: str = "phot",
        image_photometric_catalog_purifier: Callable[
            [Table, Image], Table
        ] = default_image_sextractor_catalog_purifier,
        num_matches_threshold: int = 5,
        crossmatch_radius_arcsec: float = 1.0,
        write_regions: bool = False,
        cache: bool = False,
        outlier_rejection_threshold: float | list[float] = 3.0,
    ):
        super().__init__(
            ref_catalog_generator=ref_catalog_generator,
            temp_output_sub_dir=temp_output_sub_dir,
            crossmatch_radius_arcsec=crossmatch_radius_arcsec,
            sextractor_catalog_purifier=image_photometric_catalog_purifier,
            write_regions=write_regions,
            cache=cache,
            required_parameters=REQUIRED_PARAMETERS,
        )
        self.num_matches_threshold = num_matches_threshold
        self.outlier_rejection_threshold = outlier_rejection_threshold
        if isinstance(outlier_rejection_threshold, float):
            self.outlier_rejection_threshold = [outlier_rejection_threshold]
        self.outlier_rejection_threshold = np.sort(self.outlier_rejection_threshold)

    def __str__(self) -> str:
        return "Processor to perform photometric calibration."

    def get_phot_output_dir(self):
        """
        Return the
        :return:
        """
        return get_output_dir(self.temp_output_sub_dir, self.night_sub_dir)

    def calculate_zeropoint(
        self,
        ref_cat: Table,
        clean_img_cat: Table,
    ) -> list[dict]:
        """
        Function to calculate zero point from two catalogs
        Args:
            ref_cat: Reference catalog table
            clean_img_cat: Catalog of sources from image to xmatch with ref_cat
        Returns:
        """

        matched_img_cat, matched_ref_cat, _ = self.xmatch_catalogs(
            ref_cat=ref_cat,
            image_cat=clean_img_cat,
            crossmatch_radius_arcsec=self.crossmatch_radius_arcsec,
        )
        logger.debug(
            f"Cross-matched {len(matched_img_cat)} sources from catalog to the image."
        )

        if len(matched_img_cat) < self.num_matches_threshold:
            err = (
                "Not enough cross-matched sources "
                "found to calculate a reliable zeropoint. "
                f"Only found {len(matched_img_cat)} crossmatches, "
                f"while {self.num_matches_threshold} are required. "
                f"Used {len(ref_cat)} reference sources and "
                f"{len(clean_img_cat)} image sources."
            )
            logger.error(err)
            raise PhotometryCrossMatchError(err)

        apertures = self.get_sextractor_apertures()  # aperture diameters
        zeropoints = []

        for i, aperture in enumerate(apertures):
            offsets = np.ma.array(
                matched_ref_cat["magnitude"] - matched_img_cat["MAG_APER"][:, i]
            )
            for outlier_thresh in self.outlier_rejection_threshold:
                cl_offset = sigma_clip(offsets, sigma=outlier_thresh)
                num_stars = np.sum(np.invert(cl_offset.mask))

                zp_mean, zp_med, zp_std = sigma_clipped_stats(
                    offsets, sigma=outlier_thresh
                )

                if num_stars > self.num_matches_threshold:
                    break

            check = [np.isnan(x) for x in [zp_mean, zp_med, zp_std]]
            if np.sum(check) > 0:
                err = (
                    f"Error with nan when calculating sigma stats: \n "
                    f"mean: {zp_mean}, median: {zp_med}, std: {zp_std}"
                )
                logger.error(err)
                raise PhotometryCalculationError(err)

            zero_dict = {
                "diameter": aperture,
                "zp_mean": zp_mean,
                "zp_median": zp_med,
                "zp_std": zp_std,
                "nstars": num_stars,
                "mag_cat": matched_ref_cat["magnitude"][np.invert(cl_offset.mask)],
                "mag_apers": matched_img_cat["MAG_APER"][:, i][
                    np.invert(cl_offset.mask)
                ],
            }
            zeropoints.append(zero_dict)

        for outlier_thresh in self.outlier_rejection_threshold:
            offsets = np.ma.array(
                matched_ref_cat["magnitude"] - matched_img_cat["MAG_AUTO"]
            )
            cl_offset = sigma_clip(offsets, sigma=outlier_thresh)
            num_stars = np.sum(np.invert(cl_offset.mask))
            zp_mean, zp_med, zp_std = sigma_clipped_stats(offsets, sigma=outlier_thresh)
            zero_auto_mag_cat = matched_ref_cat["magnitude"][np.invert(cl_offset.mask)]
            zero_auto_mag_img = matched_img_cat["MAG_AUTO"][np.invert(cl_offset.mask)]

            if num_stars > self.num_matches_threshold:
                break

        zeropoints.append(
            {
                "diameter": "AUTO",
                "zp_mean": zp_mean,
                "zp_median": zp_med,
                "zp_std": zp_std,
                "nstars": num_stars,
                "mag_cat": zero_auto_mag_cat,
                "mag_apers": zero_auto_mag_img,
            }
        )

        return zeropoints

    def _apply_to_images(
        self,
        batch: ImageBatch,
    ) -> ImageBatch:
        phot_output_dir = self.get_phot_output_dir()
        phot_output_dir.mkdir(parents=True, exist_ok=True)

        for image in batch:
            ref_cat, _, cleaned_img_cat = self.setup_catalogs(image)

            fwhm_med, _, fwhm_std, med_fwhm_pix, _, _ = get_fwhm(cleaned_img_cat)

            header_map = {
                "FWHM_MED": fwhm_med,
                "FWHM_STD": fwhm_std,
                "FWHM_PIX": med_fwhm_pix,
            }
            for key, value in header_map.items():
                if np.isnan(value):
                    value = -999.0
                image.header[key] = value

            if len(ref_cat) < self.num_matches_threshold:
                err = (
                    f"Not enough sources ({len(ref_cat)} found in reference catalog "
                    f"to calculate a reliable zeropoint. "
                    f"Require at least {self.num_matches_threshold} matches."
                )
                logger.error(err)
                raise PhotometryReferenceError(err)

            logger.debug(f"Found {len(cleaned_img_cat)} clean sources in image.")

            if len(cleaned_img_cat) < self.num_matches_threshold:
                err = (
                    f"Not enough sources ({len(cleaned_img_cat)} "
                    f"found in source catalog "
                    f"to calculate a reliable zeropoint. "
                    f"Require at least {self.num_matches_threshold} matches."
                )
                logger.error(err)
                raise PhotometrySourceError(err)

            zp_dicts = self.calculate_zeropoint(
                ref_cat=ref_cat, clean_img_cat=cleaned_img_cat
            )

            aperture_diameters = []
            zp_values = []

            with warnings.catch_warnings(record=True):
                warnings.simplefilter("ignore", category=VerifyWarning)

                for zpvals in zp_dicts:
                    image[f"ZP_{zpvals['diameter']}"] = zpvals["zp_mean"]
                    image[f"ZP_{zpvals['diameter']}_std"] = zpvals["zp_std"]
                    image[f"ZP_{zpvals['diameter']}_nstars"] = zpvals["nstars"]
                    try:
                        aperture_diameters.append(float(zpvals["diameter"]))
                        zp_values.append(zpvals["zp_mean"])
                    except ValueError:
                        continue

                aperture_diameters.append(med_fwhm_pix * 2)
                zp_values.append(image["ZP_AUTO"])

                if sextractor_checkimg_map["BACKGROUND_RMS"] in image.header.keys():
                    logger.debug(
                        "Calculating limiting magnitudes from background RMS file"
                    )
                    limmags = get_maglim(
                        image[sextractor_checkimg_map["BACKGROUND_RMS"]],
                        zp_values,
                        np.array(aperture_diameters) / 2.0,
                    )
                else:
                    limmags = [-99] * len(aperture_diameters)

                for ind, diam in enumerate(aperture_diameters[:-1]):
                    image[f"MAGLIM_{np.rint(diam)}"] = limmags[ind]
                image[MAGLIM_KEY] = limmags[-1]

                image[ZP_KEY] = image["ZP_AUTO"]
                image[ZP_STD_KEY] = image["ZP_AUTO_STD"]
                image[ZP_NSTARS_KEY] = image["ZP_AUTO_NSTARS"]
                image["MAGSYS"] = "AB"

        return batch
