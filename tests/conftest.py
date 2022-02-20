import logging

import pytest

from logger import set_logger_level


@pytest.fixture(scope="session", autouse=True)
def do_something():
    set_logger_level(logging.INFO)
