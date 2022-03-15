import inspect
import logging
import os
from pathlib import Path
import sys

log = logging.getLogger(__name__)

PYALANYSIS_DIR: str = "pyalanysis"


def get_cache_dir() -> Path:
    """Locate a platform-appropriate cache directory for pyalanysis to use

    Does not ensure that the cache directory exists.
    """
    log.info("Called " + inspect.stack()[0][3])

    # Linux, Unix, AIX, etc.
    if os.name == "posix" and sys.platform != "darwin":
        # use ~/.cache if empty OR not set
        pyalanysis_path = os.environ.get(
            "PYALANYSIS_CACHE", None
        ) or os.path.expanduser("~/.cache")
        return Path(pyalanysis_path, PYALANYSIS_DIR)
    # Mac OS
    elif sys.platform == "darwin":
        return Path(os.path.expanduser("~"), f"Library/Caches/{PYALANYSIS_DIR}")
    # Windows (hopefully)
    else:
        local = os.environ.get("LOCALAPPDATA", None) or os.path.expanduser(
            "~\\AppData\\Local"
        )
        return Path(local, PYALANYSIS_DIR)


def ensure_cache_dir() -> Path:
    """Locates and return an existing cache dir

    If the cache dir doesn't exist it creates the directory"""
    cache_dir = get_cache_dir()

    log.info("Called " + inspect.stack()[0][3])

    if not os.path.isdir(cache_dir):
        log.debug(f"Couldn't find dir {cache_dir}")
        log.info("Attempting to create it")

        cache_dir.mkdir(parents=True, exist_ok=True)
    else:
        log.debug(f"Found cache dir {cache_dir}")

    return cache_dir
