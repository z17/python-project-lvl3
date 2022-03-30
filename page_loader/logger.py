import logging

import logging.config

logging.basicConfig(level=logging.INFO)


def get_logger(name: str = None) -> logging.Logger:
    return logging.getLogger(name)


def set_logger_level(level):
    logger = get_logger()

    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)
