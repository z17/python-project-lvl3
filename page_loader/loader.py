import requests

from page_loader.logger import get_logger

logger = get_logger(__name__)


def load_url(url: str) -> str:
    logger.info("download text %s", url)
    page = requests.get(url)
    return page.text


def load_url_content(url: str):
    logger.info("download content %s", url)
    page = requests.get(url)
    return page.content
