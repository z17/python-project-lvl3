import logging

from pathlib import Path
import logging.config

conf_path = Path(__file__).parent.parent.joinpath('logger.conf').absolute()
logging.config.fileConfig(fname=conf_path)


def get_logger(name: str = None) -> logging.Logger:
    return logging.getLogger(name)


def set_logger_level(level):
    logger = get_logger()

    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)
