import logging

import logging.config


def get_logger(name: str = None) -> logging.Logger:
    return logging.getLogger(name)


def set_basic_config():
    logging.basicConfig(level=logging.INFO)


def set_logger_level(level):
    logger = get_logger()

    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)
