import logging
from logging import StreamHandler

from vic_lim_wx.custom_logger.public.logger_config import \
    LoggerConfig
from vic_lim_wx.custom_logger.private_repo.colored_formatter import \
    ColoredFormatter


class LoggerFactory:
    def __init__(self, config_file_path):
        self.config = LoggerConfig(config_file_path)

    def create_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        handler = StreamHandler()
        handler.setLevel(logging.DEBUG)

        formatter = ColoredFormatter(self.config.get_format())
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger
