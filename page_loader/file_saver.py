import string
from pathlib import Path

from page_loader.logger import get_logger

logger = get_logger(__name__)


def save_page(file_path: Path, content: string):
    with file_path.open('w') as file:
        file.write(content)
        logger.info("page saved to %s", str(file_path))


def save_resource(file_path: Path, data):
    with open(file_path, 'wb') as handler:
        handler.write(data)
        logger.info("resource saved to %s", str(file_path))

