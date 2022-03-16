import os
import shutil
import tempfile
from typing import cast
from unittest import mock, TestCase
from unittest.mock import Mock

from pyalanysis.utils import ensure_cache_dir, get_cache_dir  # type: ignore


class TestGetCacheDir(TestCase):
    _tempdir: str = (tempfile.tempdir or "/tmp") + "/test_pyalanysis"

    def setUp(self):
        if os.name == "posix":
            if os.path.exists(self._tempdir):
                shutil.rmtree(self._tempdir)

    @mock.patch.dict(
        os.environ,
        {"PYALANYSIS_MINES_USERNAME": ""},
    )
    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    @mock.patch("os.makedirs", mock.Mock(return_value=0))
    def test_get_cache_dir(self) -> None:
        if os.name == "posix":
            get_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)
            makedirs = cast(Mock, os.makedirs)

            assert mock_expanduser.called
            assert not makedirs.called

    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    @mock.patch("sys.platform", "Darwin")
    def test_get_cache_dir_mac(self) -> None:
        get_cache_dir()

        mock_expanduser = cast(Mock, os.path.expanduser)
        assert mock_expanduser.called

    @mock.patch.dict(
        os.environ,
        {"PYALANYSIS_MINES_USERNAME": ""},
    )
    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    @mock.patch("sys.platform", "win64")
    def test_get_cache_dir_mac(self) -> None:
        get_cache_dir()

        mock_expanduser = cast(Mock, os.path.expanduser)
        assert mock_expanduser.called


class TestEnsureDir(TestCase):
    _tempdir: str = (tempfile.tempdir or "/tmp") + "/test_pyalanysis"

    def setUp(self):
        if os.name == "posix":
            if os.path.exists(self._tempdir):
                shutil.rmtree(self._tempdir)

    @mock.patch.dict(
        os.environ,
        {"PYALANYSIS_MINES_USERNAME": ""},
    )
    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    def test_ensure_cache_dir_new_dir(self) -> None:
        if os.name == "posix":
            ensure_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)

            assert mock_expanduser
            assert os.path.exists(self._tempdir)

    @mock.patch.dict(
        os.environ,
        {"PYALANYSIS_MINES_USERNAME": ""},
    )
    @mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
    def test_ensure_cache_dir_existing_dir(self) -> None:
        if os.name == "posix":
            cache_dir = get_cache_dir()
            cache_dir.mkdir(parents=True, exist_ok=True)

            assert cache_dir == ensure_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)

            assert mock_expanduser
            assert os.path.exists(self._tempdir)

    def tearDown(self) -> None:
        if os.name == "posix":
            if os.path.exists(self._tempdir):
                shutil.rmtree(self._tempdir)
