import logging
import logging.config
from typing import List

from pyalanysis.data import ViirsDnbMonthly
from pyalanysis.data import ViirsDnbMonthlyType

MY_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default_formatter": {"format": "[%(levelname)s:%(asctime)s] %(message)s"},
    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "default_formatter",
        },
    },
    "loggers": {
        "mylogger": {"handlers": ["stream_handler"], "level": "INFO", "propagate": True}
    },
}

logging.config.dictConfig(MY_LOGGING_CONFIG)
logger = logging.getLogger(__name__)

__version__ = "0.1.002"


__all__: List[str] = ["ViirsDnbMonthly", "ViirsDnbMonthlyType"]
