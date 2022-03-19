import requests

from page_loader.logger import get_logger

logger = get_logger(__name__)


def load_url(url: str) -> str:
    logger.info("downloading text %s", url)
    page = load(url)
    return page.text


def load_url_content(url: str):
    logger.info("downloading content %s", url)
    page = load(url)
    return page.content


def load(url: str):
    try:
        result = requests.get(url)
        if result.status_code != requests.codes.ALL_GOOD:
            logger.error("Status code %s for %s", result.status_code, url)
            raise RuntimeError("Status code %s for %s", result.status_code, url)
        return result
    except requests.exceptions.ConnectionError:
        logger.error("Connection error to %s", url)
        raise RuntimeError("Connection error to %s", url)
