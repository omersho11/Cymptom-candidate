import logging
from constants import LOG_FORMAT, LOG_FILE_PATH


class Logger:
    def __init__(self):
        self.logger = logging.getLogger('main_logger')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(LOG_FILE_PATH)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        fh.setFormatter(logging.Formatter(LOG_FORMAT))
        ch.setFormatter(logging.Formatter(LOG_FORMAT))
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)