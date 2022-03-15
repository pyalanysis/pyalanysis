import os
import re
from unittest import mock

from pyalanysis.data import get_viirs_dnb_monthly_file, get_viirs_dnb_monthly_fn, ViirsDnbMonthlyType  # type: ignore
from pyalanysis.utils import ensure_cache_dir  # type: ignore
import responses  # type: ignore

from .viirsdnb_utils import mines_dir_listing_monthly, mines_login_form, mines_login_form_post  # type: ignore


@responses.activate
def test_get_viirs_dnb_monthly_fn():
    responses.add(
        mines_dir_listing_monthly.method,
        url=mines_dir_listing_monthly.url,
        body=mines_dir_listing_monthly.html_content,
        status=200,
        content_type="application/html",
    )

    assert get_viirs_dnb_monthly_fn(
        "00N060E", 1900, 9, ViirsDnbMonthlyType.STRAY_LIGHT_CORRECTED
    ) == (
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg/"
        + "SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz",
        "SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz",
    )


@mock.patch.dict(
    os.environ,
    {"PYALANYSIS_MINES_USERNAME": "usertest", "PYALANYSIS_MINES_PASSWORD": "userpass"},
)
@responses.activate
def test_get_viirs_dnb_monthly_file():
    responses.add(
        mines_dir_listing_monthly.method,
        url=mines_dir_listing_monthly.url,
        body=mines_dir_listing_monthly.html_content,
        status=200,
        content_type="application/html",
    )

    responses.add(
        mines_login_form.method,
        url=re.compile(
            "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg/.*"
        ),
        body=mines_login_form.html_content,
        status=200,
        content_type="application/html",
    )
    responses.add(
        mines_login_form_post.method,
        url=mines_login_form_post.url,
        body="",
        status=200,
        content_type="application/tar+gz",
    )

    assert get_viirs_dnb_monthly_file(
        "00N060E", 1900, 9, ViirsDnbMonthlyType.STRAY_LIGHT_CORRECTED
    ) == (
        str(ensure_cache_dir())
        + "/SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz"
    )
