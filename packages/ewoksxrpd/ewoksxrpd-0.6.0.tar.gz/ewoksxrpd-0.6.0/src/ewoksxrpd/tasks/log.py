import logging
import time
from typing import Iterator, Optional

_logger = logging.getLogger(__name__)


def log_iterator_progress(
    message: str = "Progress %d/%s",
    nmax: Optional[int] = None,
    period: float = 5,
    logger=None,
) -> Iterator:
    if logger is None:
        logger = _logger
    i = 0
    t0 = time.time()
    if nmax is None:
        nmax = "?"
    try:
        while True:
            yield
            i += 1
            if (time.time() - t0) > period:
                t0 = time.time()
                _logger.info(message, i, nmax)
    finally:
        _logger.info(f"{message} (FINISHED)", i, nmax)
