import os
from pathlib import Path
import shutil
import tempfile
from typing import Callable, cast
from unittest import mock
from unittest.mock import Mock
import warnings

from pyalanysis.utils import ensure_cache_dir, get_cache_dir  # type: ignore


def get_secure_tempdir():
    dir_ = tempfile.mkdtemp() or "/tmp" + "/test_pyalanysis"  # type: ignore  # noqa: S108
    os.chmod(dir_, 0o700)
    return dir_


_tempdir = get_secure_tempdir()


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


@gen_cache_dir(_tempdir)
@mock.patch("os.makedirs", mock.Mock(return_value=0))
def test_get_cache_dir() -> None:
    if os.name == "posix":
        get_cache_dir()

        mock_expanduser = cast(Mock, os.path.expanduser)
        makedirs = cast(Mock, os.makedirs)

        assert mock_expanduser.called
        assert not makedirs.called


@gen_cache_dir(_tempdir)
@mock.patch("sys.platform", "darwin")
def test_get_cache_dir_mac() -> None:
    get_cache_dir()

    mock_expanduser = cast(Mock, os.path.expanduser)
    assert mock_expanduser.called


@mock.patch("os.path.expanduser", mock.Mock(return_value=_tempdir))
@mock.patch("sys.platform", "win64")
@mock.patch("os.name", "win64")
def test_get_cache_dir_win() -> None:
    cache_dir = get_cache_dir()

    mock_expanduser = cast(Mock, os.path.expanduser)
    assert mock_expanduser.called
    assert cache_dir == Path(f"{_tempdir}/pyalanysis")


@gen_cache_dir(_tempdir)
def test_ensure_cache_dir_new_dir() -> None:
    if os.name == "posix":
        cache_dir = ensure_cache_dir()

        mock_expanduser = cast(Mock, os.path.expanduser)

        assert mock_expanduser
        assert os.path.exists(cache_dir)


@gen_cache_dir(_tempdir)
def test_ensure_cache_dir_existing_dir() -> None:
    if os.name == "posix":
        cache_dir = get_cache_dir()
        cache_dir.mkdir(parents=True, exist_ok=True)

        assert cache_dir == ensure_cache_dir()

        mock_expanduser = cast(Mock, os.path.expanduser)

        assert mock_expanduser
        assert os.path.exists(cache_dir)
