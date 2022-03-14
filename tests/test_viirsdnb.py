# import unittest

from pyalanysis.data import get_viirs_dnb_monthly_fn, ViirsDnbMonthlyType


def test_get_viirs_dnb_monthly_fn():
    assert get_viirs_dnb_monthly_fn(
        "00N060E", 2021, 9, ViirsDnbMonthlyType.STRAY_LIGHT_CORRECTED
    ) == (
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/2021/202109/vcmslcfg/"
        + "SVDNB_npp_20210901-20210930_00N060E_vcmslcfg_v10_c202110112300.tgz"
    )
