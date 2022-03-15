from dataclasses import dataclass
import inspect
from enum import Enum
import logging
from pathlib import Path
from typing import Callable, List, Tuple, Optional
import os

import bs4
import mechanicalsoup as ms

from pyalanysis.utils import ensure_cache_dir

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


class ViirsDnbMonthlyType(Enum):
    """Defines what type stray light correction is applied"""

    STRAY_LIGHT_CORRECTED = 1
    NO_STRAY_LIGHT = 2


@dataclass
class ViirsDnbMonthly:
    """Class to load monthly VIIRS DNB data"""

    def __init__(
        self,
        region: str,
        year: int,
        month: int,
        stray_light_treatment: ViirsDnbMonthlyType,
    ):
        self.region: str = region
        self.year: int = year
        self.month: int = month
        self.stray_light: ViirsDnbMonthlyType = stray_light_treatment


def get_viirs_dnb_monthly_fn(
    region: str, year: int, month: int, stray_light_treatment: ViirsDnbMonthlyType
) -> Tuple[str, str]:
    log.info("Called " + inspect.stack()[0][3])
    format_type: Callable[[ViirsDnbMonthlyType], str] = (
        lambda type: "vcmcfg"
        if type == ViirsDnbMonthlyType.NO_STRAY_LIGHT
        else "vcmslcfg"
    )

    url = (
        MINES_SITE
        + f"monthly/v10/{year}/{year}{month:02}/{format_type(stray_light_treatment)}"
    )

    browser: ms.stateful_browser.StatefulBrowser = ms.StatefulBrowser(raise_on_404=True)

    try:
        browser.open(url)
        links: bs4.element.ResultSet = browser.page.findAll("a")
        fn: str = ""
        i: bs4.element.Tag

        for i in links:
            if "href" in i.attrs.keys():
                if i.attrs["href"].startswith("SVDNB"):
                    fn = i.attrs["href"]
                    break

        log.info(f"Retrieved {fn} from {url}")

        if fn == "":
            raise Exception(f"No SVDNB found at url '{url}'")

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
    region: str, year: int, month: int, stray_light_treatment: ViirsDnbMonthlyType
) -> str:
    """Either downloads or gets the VIIRS DNB Monthly file from local cache and return the path

    """
    log.info("Called " + inspect.stack()[0][3])

    url_to_get, fn = get_viirs_dnb_monthly_fn(region, year, month, stray_light_treatment)

    log.info("Test to find if the file exist in the cache dir")
    cache_dir: Path = ensure_cache_dir()

    output_fn: str = os.path.join(cache_dir, fn)
    if os.path.isfile(output_fn):
        return output_fn
    else:
        log.info("Seek to get data from " + url_to_get)
        browser: ms.stateful_browser.StatefulBrowser = ms.StatefulBrowser(raise_on_404=True)

        try:
            browser.open(url_to_get)
           # links: bs4.element.ResultSet = browser.page.findAll("a")
            mines_username_env:Optional[str] = os.getenv("PYALANYSIS_MINES_USERNAME")
            mines_password_env:Optional[str] = os.getenv("PYALANYSIS_MINES_PASSWORD")

            if mines_username_env is None:
                raise Exception("Coudn't find env setting PYALANYSIS_MINES_USERNAME")
            else:
                mines_username: str = mines_username_env

            if mines_password_env is None:
                raise Exception("Coudn't find env setting PYALANYSIS_MINES_PASSWORD")
            else:
                mines_password: str = mines_password_env


            log.info(f"Trying to login with username:password {mines_username}:####### ")
            browser.select_form("#kc-form-login")
            browser["username"] = mines_username
            browser["password"] = mines_password

            resp = browser.submit_selected()
            log.info("Raising for any status we may have other than 200")
            resp.raise_for_status()

            log.info(f"Save data to {output_fn}")
            with open(output_fn, "wb") as outf:
                outf.write(resp.content)


        except Exception as e:
            logging.error(e)
            raise

        return output_fn
