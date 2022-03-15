from dataclasses import dataclass
from enum import Enum
import logging
from typing import Callable, List

import bs4
import mechanicalsoup as ms

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
) -> str:
    logging.info("Called " + __name__)
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

        logging.info(f"Retrieved {fn} from {url}")

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
    return url + "/" + fn_to_get


def get_viirs_dnb_monthly(
    region: str, year: int, month: int, stray_light_treatment: ViirsDnbMonthlyType
) -> ViirsDnbMonthly:
    logging.info("Called " + __name__)

    url_to_get = get_viirs_dnb_monthly_fn(region, year, month, stray_light_treatment)
    logging.info("Seek to get data from " + url_to_get)

    return ViirsDnbMonthly(region, year, month, stray_light_treatment)
