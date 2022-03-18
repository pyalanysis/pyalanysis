import os
import re
import shutil
from typing import Callable, cast
from unittest import mock
from unittest.mock import Mock

import mechanicalsoup
import pytest
import responses  # type: ignore

from pyalanysis.data import (
    get_viirs_dnb_monthly_file,
    get_viirs_dnb_monthly_fn,
    open_viirs_monthly_file,
    ViirsDnbMonthlyType,
)  # type: ignore
from pyalanysis.utils import ensure_cache_dir  # type: ignore
from .test_utils import gen_cache_dir, get_secure_tempdir
from .viirsdnb_utils import mines_dir_listing, mines_login_form, mines_login_form_post  # type: ignore

_tempdir: str = get_secure_tempdir()


@pytest.mark.dependency(name="test_get_viirs_dnb_monthly_fn")
@responses.activate
def test_get_viirs_dnb_monthly_fn():
    responses.add(
        mines_dir_listing["monthly_vcmslcfg"].method,
        url=mines_dir_listing["monthly_vcmslcfg"].url,
        body=mines_dir_listing["monthly_vcmslcfg"].html_content,
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

    responses.add(
        mines_dir_listing["monthly_vcmcfg"].method,
        url=mines_dir_listing["monthly_vcmcfg"].url,
        body=mines_dir_listing["monthly_vcmcfg"].html_content,
        status=200,
        content_type="application/html",
    )

    assert get_viirs_dnb_monthly_fn(
        "00N060E", 1900, 9, ViirsDnbMonthlyType.NO_STRAY_LIGHT
    ) == (
               "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmcfg/"
               + "SVDNB_npp_19000901-19000930_00N060E_vcmcfg_v10_c190010112300.tgz",
               "SVDNB_npp_19000901-19000930_00N060E_vcmcfg_v10_c190010112300.tgz",
           )




@responses.activate
def test_get_viirs_dnb_monthly_fn_error_404():
    responses.add(
        mines_dir_listing["monthly_vcmslcfg"].method,
        url=mines_dir_listing["monthly_vcmslcfg"].url,
        body=mines_dir_listing["monthly_vcmslcfg"].html_content,
        status=404,
        content_type="application/html",
    )

    with pytest.raises(mechanicalsoup.LinkNotFoundError) as excinfo:
        get_viirs_dnb_monthly_fn(
            "00N060E", 1900, 9, ViirsDnbMonthlyType.STRAY_LIGHT_CORRECTED
        )

    assert "" in str(excinfo.value)


@responses.activate
def test_get_viirs_dnb_monthly_fn_error_nolink():
    responses.add(
        mines_dir_listing["monthly_vcmslcfg"].method,
        url=mines_dir_listing["monthly_vcmslcfg"].url,
        body="<HTML><body><text>dummy</text></body></HTML>",
        status=200,
        content_type="application/html",
    )

    with pytest.raises(Exception) as excinfo:
        get_viirs_dnb_monthly_fn(
            "00N060E", 1900, 9, ViirsDnbMonthlyType.STRAY_LIGHT_CORRECTED
        )

    assert "No link found" in str(excinfo.value)




def viirs_response_local_dir(test_type: str, login_catch_url: re.Pattern) -> Callable:
    def wrap(f: Callable) -> Callable[[object], None]:
        @gen_cache_dir(_tempdir)
        @mock.patch("sys.platform", "linux")
        @mock.patch("os.name", "posix")
        @pytest.mark.dependency(
            name="test_get_viirs_dnb_monthly_file",
            depends=["test_get_viirs_dnb_monthly_fn"],
        )
        @responses.activate
        def wrapped_f(*args):
            responses.add(
                mines_dir_listing[test_type].method,
                url=mines_dir_listing[test_type].url,
                body=mines_dir_listing[test_type].html_content,
                status=200,
                content_type="application/html",
            )

            responses.add(
                mines_login_form[test_type].method,
                url=login_catch_url,
                body=mines_login_form[test_type].html_content,
                status=200,
                content_type="application/html",
            )
            responses.add(
                mines_login_form_post[test_type].method,
                url=mines_login_form_post[test_type].url,
                body="",
                status=200,
                content_type="application/tar+gz",
            )
            f(*args)

        return wrapped_f
    return wrap

class TestViirsDnbMonthlyFile:
    _loc: str = "00N060E"
    _year: int = 1900
    _month: int = 9
    _light_correction: ViirsDnbMonthlyType = ViirsDnbMonthlyType.STRAY_LIGHT_CORRECTED

    @viirs_response_local_dir("monthly_vcmslcfg", re.compile(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg/.*"
    ))
    @mock.patch.dict(
        os.environ,
        {
            "PYALANYSIS_MINES_USERNAME": "usertest",
            "PYALANYSIS_MINES_PASSWORD": "userpass",
        },
    )
    def test_get_viirs_dnb_monthly_file(self):
        fn = "SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz"
        assert get_viirs_dnb_monthly_file(
            "00N060E", 1900, 9, ViirsDnbMonthlyType.STRAY_LIGHT_CORRECTED
        ) == (str(ensure_cache_dir()) + "/" + fn, fn)

    @viirs_response_local_dir("monthly_vcmslcfg", re.compile(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg/.*"
    ))
    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    @mock.patch("mechanicalsoup.stateful_browser.StatefulBrowser", mock.Mock())
    @mock.patch.dict(
        os.environ,
        {
            "PYALANYSIS_MINES_USERNAME": "usertest",
            "PYALANYSIS_MINES_PASSWORD": "userpass",
        },
    )
    @responses.activate
    def test_get_viirs_dnb_monthly_file_file_exists(self):
        mock_statefulbrowser = cast(
            Mock, mechanicalsoup.stateful_browser.StatefulBrowser
        )

        dir = ensure_cache_dir()
        url, file = get_viirs_dnb_monthly_fn(
            self._loc, self._year, self._month, self._light_correction
        )

        with open(f"{dir}/{file}", "wb") as outf:
            outf.write(b"just a test")

        assert get_viirs_dnb_monthly_file(
            self._loc, self._year, self._month, self._light_correction
        ) == (str(ensure_cache_dir()) + "/" + file, file)
        assert not mock_statefulbrowser.called

    @mock.patch.dict(
        os.environ,
        {},
    )
    @viirs_response_local_dir("monthly_vcmslcfg", re.compile(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg/.*"
    ))
    def test_no_username(self):
        with pytest.raises(Exception) as excinfo:
            get_viirs_dnb_monthly_file(
                self._loc, self._year, self._month, self._light_correction
            )

        assert "PYALANYSIS_MINES_USERNAME" in str(excinfo.value)

    @mock.patch.dict(
        os.environ,
        {"PYALANYSIS_MINES_USERNAME": "someval"},
    )
    @viirs_response_local_dir("monthly_vcmslcfg", re.compile(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg/.*"
    ))
    def test_no_password(self):
        with pytest.raises(Exception) as excinfo:
            get_viirs_dnb_monthly_file(
                self._loc, self._year, self._month, self._light_correction
            )

        assert "PYALANYSIS_MINES_PASSWORD" in str(excinfo.value)

    def teardown(self) -> None:
        if os.name == "posix":
            if os.path.exists(_tempdir):
                shutil.rmtree(_tempdir)


class TestOpen:
    @gen_cache_dir(_tempdir)
    @mock.patch("sys.platform", "linux")
    @mock.patch("os.name", "posix")
    def test_open_viirs_dnb_monthly_vcmslcfg_load(self) -> None:
        tar_ball_name = (
            "SVDNB_npp_19001001-19001031_00N060E_vcmslcfg_v10_c190010112300.tgz"
        )
        shutil.copy(
            os.path.join(
                ".", "tests", "test_viirs_monthly_vcmslcfg_load", tar_ball_name
            ),
            _tempdir,
        )
        res = open_viirs_monthly_file(
            (os.path.join(_tempdir, tar_ball_name), tar_ball_name)
        )

        assert res.dims == {"band": 1, "x": 481, "y": 481, "time": 1}

    def teardown(self) -> None:
        if os.name == "posix":
            if os.path.exists(_tempdir):
                shutil.rmtree(_tempdir)
