from . import telescope
from . import scheduler

__version__ = "0.1b1"

# Set up logging
from loguru import logger

logger.remove()

from . import config

log_config = config.get_config_for_key("Logging") or {}
log_file = log_config.get("File")
if log_file is not None:
    log_level = log_config.get("Log Level") or "INFO"
    logger.add(
        log_file,
        format="{time} {level} {name}: {message}",
        level=log_level,
        rotation="1 week",
        retention=20,
        backtrace=True,
    )
logger.info("CTMO Manager started.")
