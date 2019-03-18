from . import telescope
from . import scheduler

__version__ = '0.1a9'

# Set up logging
from . import config

import logging
log_config = config.get_config_for_key('Logging') # or {}

logger = logging.getLogger(__name__)
level_dict = {'CRITICAL': logging.CRITICAL,
              'ERROR': logging.ERROR,
              'WARNING': logging.WARNING,
              'INFO': logging.INFO,
              'DEBUG': logging.DEBUG,
             }
log_level = level_dict.get(log_config.get('Log Level')) # or 'INFO'
logger.setLevel(log_level)

from logging.handlers import TimedRotatingFileHandler
log_dir = log_config.get('Dir') # or '/etc/ctmo/logs/ctmo.log'
import os
if not os.path.exists(log_dir):
    try:
        os.makedirs(log_dir)
    except:
        log_dir = "."
log_file_path = os.path.join(log_dir, 'ctmo.log')
log_handler = TimedRotatingFileHandler(log_file_path, when='W6', backupCount=20)
log_format = logging.Formatter("%(asctime)s [%(levelname)s] (%(name)s): %(message)s")
log_handler.setFormatter(log_format)
logger.addHandler(log_handler)
logger.info("CTMO Manager started.")
