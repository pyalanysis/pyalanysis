import os
import shutil
import tempfile
from typing import cast
import unittest
from unittest import mock
from unittest.mock import Mock

from pyalanysis.utils import ensure_cache_dir, get_cache_dir  # type: ignore


class TestUtils(unittest.TestCase):
    tempdir = (tempfile.tempdir or "/tmp") + "/test_pyalanysis"

    @mock.patch.dict(
        os.environ,
        {"PYALANYSIS_MINES_USERNAME": ""},
    )
    @mock.patch("os.path.expanduser", mock.Mock(return_value=tempdir))
    @mock.patch("os.makedirs", mock.Mock(return_value=0))
    def test_get_cache_dir(self) -> None:
        if os.name == "posix":
            get_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)
            makedirs = cast(Mock, os.makedirs)

            assert mock_expanduser.called
            assert not makedirs.called

    @mock.patch.dict(
        os.environ,
        {"PYALANYSIS_MINES_USERNAME": ""},
    )
    @mock.patch("os.path.expanduser", mock.Mock(return_value=tempdir))
    def test_ensure_cache_dir(self) -> None:
        if os.name == "posix":
            ensure_cache_dir()

            mock_expanduser = cast(Mock, os.path.expanduser)

            assert mock_expanduser
            assert os.path.exists(self.tempdir)

    def tearDown(self) -> None:
        if os.name == "posix":
            if os.path.exists(self.tempdir):
                shutil.rmtree(self.tempdir)
