import os
from pathlib import Path
import shutil
import tempfile
from typing import cast, Callable
from unittest import mock, TestCase
from unittest.mock import Mock
import warnings

import logging

from pyalanysis.utils import ensure_cache_dir, get_cache_dir  # type: ignore

_tempdir: str = (tempfile.mkdtemp() or "/tmp") + "/test_pyalanysis"


def gen_cache_dir(cache_location: str) -> Callable:
    def wrap(f):
        @mock.patch("os.path.expanduser", mock.Mock(return_value=cache_location))
        @mock.patch("sys.platform", "linux")
        def wrapped_f(*args):
            if os.name == "posix":
                mock_cache_dir = ensure_cache_dir()

                f(*args)

                shutil.rmtree(mock_cache_dir)
            else:
                warnings.warn("Don't support other than posix at the moment")

        return wrapped_f

    return wrap


class TestGetCacheDir(TestCase):
    def setUp(self):
        if os.name == "posix":
            if os.path.exists(_tempdir):
                shutil.rmtree(_tempdir)

    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    @mock.patch("os.makedirs", mock.Mock(return_value=0))
    @mock.patch("sys.platform", "linux")
    def test_get_cache_dir(self) -> None:
        if os.name == "posix":
            get_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)
            makedirs = cast(Mock, os.makedirs)

            assert mock_expanduser.called
            assert not makedirs.called

    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    @mock.patch("sys.platform", "darwin")
    def test_get_cache_dir_mac(self) -> None:
        get_cache_dir()

        mock_expanduser = cast(Mock, os.path.expanduser)
        assert mock_expanduser.called

    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    @mock.patch("sys.platform", "win64")
    @mock.patch("os.name", "win64")
    def test_get_cache_dir_win(self) -> None:
        cache_dir = get_cache_dir()

        mock_expanduser = cast(Mock, os.path.expanduser)
        assert mock_expanduser.called
        assert cache_dir == Path(f"{_tempdir}/pyalanysis")


class TestEnsureDir(TestCase):
    _tempdir: str = (tempfile.tempdir or "/tmp") + "/test_pyalanysis"

    def setUp(self):
        if os.name == "posix":
            if os.path.exists(_tempdir):
                shutil.rmtree(_tempdir)

    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    def test_ensure_cache_dir_new_dir(self) -> None:
        if os.name == "posix":
            cache_dir = ensure_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)

            assert mock_expanduser
            assert os.path.exists(cache_dir)

    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    def test_ensure_cache_dir_existing_dir(self) -> None:
        if os.name == "posix":
            cache_dir = get_cache_dir()
            cache_dir.mkdir(parents=True, exist_ok=True)

            assert cache_dir == ensure_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)

            assert mock_expanduser
            assert os.path.exists(cache_dir)

    def teardown(self) -> None:
        if os.name == "posix":
            if os.path.exists(_tempdir):
                shutil.rmtree(_tempdir)
