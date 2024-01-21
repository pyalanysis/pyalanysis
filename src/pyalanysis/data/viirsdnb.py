from enum import Enum
import inspect
import logging
import os
from pathlib import Path
import tarfile
from typing import List, Optional, Tuple

import bs4
import mechanicalsoup as ms
import pandas as pd
import rioxarray  # type: ignore
import xarray as xr

from pyalanysis.utils import (
    all_files_exist,
    ensure_cache_dir,
)

log = logging.getLogger(__name__)

MINES_SITE = "https://eogdata.mines.edu/nighttime_light/"

# See for filename explanation [1]
# [1]: https://data.ngdc.noaa.gov/instruments/remote-sensing/passive/spectrometers-radiometers/imaging/viirs/\
#       dnb_composites/v10/README_dnb_composites_v1.txt
MINES_FN_SAT_TOKEN_LOC = 1
MINES_FN_DATE_RANGE_TOKEN_LOC = 2
MINES_FN_ROI_TOKEN_LOC = 3
MINES_FN_CONFIG_TOKEN_LOC = 4
MINES_FN_VERSION_TOKEN_LOC = 5
MINES_FN_CREATION_DATE_TOKEN_LOC = 6

FILE_EXTENSION_AVG_RAD = ".avg_rade9h.tif"
FILE_EXTENSION_NUM_OBS = ".cvg.tif"
FILE_EXTENSION_NUM_CLOUD_FREE_OBS = ".cf_cvg.tif"


class ViirsDnbMonthlyType(Enum):
    """Defines what type stray light correction is applied"""

    STRAY_LIGHT_CORRECTED = 1
    NO_STRAY_LIGHT = 2


class ViirsDnbMonthlyDataLoader:
    def __init__(self):
        self._browser: ms.stateful_browser.StatefulBrowser = ms.StatefulBrowser(
            raise_on_404=True
        )

    def get_viirs_dnb_monthly_fn(
        self,
        region: str,
        year: int,
        month: int,
        stray_light_treatment: ViirsDnbMonthlyType,
    ) -> Tuple[str, str]:
        format_type = (
            "vcmcfg"
            if stray_light_treatment == ViirsDnbMonthlyType.NO_STRAY_LIGHT
            else "vcmslcfg"
        )

        url = MINES_SITE + f"monthly/v10/{year}/{year}{month:02}/{format_type}"

        try:
            self._browser.open(url)
            links: bs4.element.ResultSet = self._browser.page.findAll("a")
            fn: str = ""
            i: bs4.element.Tag

            for i in links:
                if "href" in i.attrs.keys():
                    if i.attrs["href"].startswith("SVDNB"):
                        fn = i.attrs["href"]
                        break

            log.info(f"Retrieved {fn} from {url}")

            if fn == "":
                log.error(f"Couldn't find a link at {url}")
                raise Exception("No link found")

        except Exception as e:
            logging.error(e)
            raise

        fn_tokens: List[str] = fn.split("_")
        fn_to_get: str = "_".join(
            [
                "SVDNB",
                fn_tokens[MINES_FN_SAT_TOKEN_LOC],
                fn_tokens[MINES_FN_DATE_RANGE_TOKEN_LOC],
                region,
                fn_tokens[MINES_FN_CONFIG_TOKEN_LOC],
                fn_tokens[MINES_FN_VERSION_TOKEN_LOC],
                fn_tokens[MINES_FN_CREATION_DATE_TOKEN_LOC],
            ]
        )
        return url + "/" + fn_to_get, fn_to_get

    def get_viirs_dnb_monthly_file(
        self,
        region: str,
        year: int,
        month: int,
        stray_light_treatment: ViirsDnbMonthlyType,
    ) -> Tuple[str, str]:
        """Either downloads or gets the VIIRS DNB Monthly file from local cache and return the path"""
        url_to_get, fn = self.get_viirs_dnb_monthly_fn(
            region, year, month, stray_light_treatment
        )

        log.info("Test to find if the file exist in the cache dir")
        cache_dir: Path = ensure_cache_dir()

        output_fp: str = os.path.join(cache_dir, fn)
        if os.path.isfile(output_fp):
            log.info("Found file in cache dir")
            return output_fp, fn
        else:
            log.info("Seek to get data from " + url_to_get)

            try:
                self._browser.open(url_to_get)
                # links: bs4.element.ResultSet = browser.page.findAll("a")
                mines_username_env: Optional[str] = os.getenv(
                    "PYALANYSIS_MINES_USERNAME"
                )
                mines_password_env: Optional[str] = os.getenv(
                    "PYALANYSIS_MINES_PASSWORD"
                )

                if mines_username_env is None:
                    raise Exception(
                        "Coudn't find env setting PYALANYSIS_MINES_USERNAME"
                    )
                else:
                    mines_username: str = mines_username_env

                if mines_password_env is None:
                    raise Exception(
                        "Coudn't find env setting PYALANYSIS_MINES_PASSWORD"
                    )
                else:
                    mines_password: str = mines_password_env

                log.info(
                    f"Trying to login with username:password {mines_username}:####### "
                )
                self._browser.select_form("#kc-form-login")
                self._browser["username"] = mines_username
                self._browser["password"] = mines_password

                resp = self._browser.submit_selected()
                log.info("Raising for any status we may have other than 200")
                resp.raise_for_status()

                log.info(f"Save data to {output_fp}")
                with open(output_fp, "wb") as outf:
                    outf.write(resp.content)

            except Exception as e:
                logging.error(e)
                raise

            return output_fp, fn

    def open_viirs_monthly_file(
        self, filespec: Tuple[str, str], only_avg_rad9h=False, **kwargs
    ):
        log.info("Called " + inspect.stack()[0][3])
        base_fn = filespec[1].split(".")[0]
        dst_dir_name = os.path.join(ensure_cache_dir(), base_fn)

        expected_ext = [
            FILE_EXTENSION_AVG_RAD,
            FILE_EXTENSION_NUM_OBS,
            FILE_EXTENSION_NUM_CLOUD_FREE_OBS,
        ]
        base_path = f"{dst_dir_name}/{base_fn}"
        expected_files = [f"{base_path}{ext}" for ext in expected_ext]

        if not all_files_exist(expected_files):
            log.debug(
                "Didn't find all expected files, falling back on opening tar ball"
            )
            tarball = tarfile.open(filespec[0])
            log.debug(f"Attempt to extract tar ball {filespec[0]} in {dst_dir_name}")
            tarball.extractall(dst_dir_name)
            tarball.close()
        else:
            log.debug("Found all expected files")

        log.debug("Continuing to load all geotiff data")

        fn_tokens = base_fn.split("_")

        avg_rad9h = rioxarray.open_rasterio(
            base_path + FILE_EXTENSION_AVG_RAD, mask_and_scale=False, **kwargs
        )
        avg_rad9h.name = "avg_rad9h"
        if not only_avg_rad9h:
            cvg = rioxarray.open_rasterio(
                base_path + FILE_EXTENSION_NUM_OBS, mask_and_scale=False, **kwargs
            )
            cvg.name = "cvg"
            cf_cvg = rioxarray.open_rasterio(
                base_path + FILE_EXTENSION_NUM_CLOUD_FREE_OBS,
                mask_and_scale=False,
                **kwargs,
            )
            cf_cvg.name = "cf_cvg"

            new_ds = xr.merge([avg_rad9h, cvg, cf_cvg])
        else:
            new_ds = avg_rad9h.to_dataset()

        year = int(fn_tokens[MINES_FN_DATE_RANGE_TOKEN_LOC][0:4])
        month = int(fn_tokens[MINES_FN_DATE_RANGE_TOKEN_LOC][4:6])
        start = int(fn_tokens[MINES_FN_DATE_RANGE_TOKEN_LOC][6:8])
        time_range = pd.date_range(f"{year}-{month}-{start}", freq="MS", periods=1)

        log.debug(f"Creating xarray for {year}, {month}, start {start}")

        return new_ds.expand_dims("time").assign_coords(time=("time", time_range))
