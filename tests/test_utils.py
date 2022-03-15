import inspect
import logging
import os
import sys
from unittest import mock

from pyalanysis.utils import ensure_cache_dir  # type: ignore
import pytest


log = logging.getLogger(__name__)

class MockPathCall:
    def __init__(self, called:bool=False):
        self._called = called

    def call(self, *args) -> str:
        log.info("Called " + inspect.stack()[0][3])
        self._called = not self._called

        return "/tmp"

    @property
    def called(self) -> bool:
        return self._called


@mock.patch.dict(
    os.environ,
    {"PYALANYSIS_MINES_USERNAME": ""},
)
@mock.patch('os.makedirs', mock.Mock(return_value=0))
def test_get_cache_dir(mocker):
    called_os_path_expander = MockPathCall()
    mocker.patch("os.path.expanduser", side_effect=called_os_path_expander.call)

    ensure_cache_dir()

    if os.name == "posix":
        assert called_os_path_expander.called
        assert not os.makedirs.called

