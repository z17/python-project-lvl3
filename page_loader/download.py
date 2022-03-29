import string
from pathlib import Path

from page_loader.Progress import Progress
from page_loader.file_paths import get_page_download_path
from page_loader.file_saver import save_page
from page_loader.loader import load_url
from page_loader.logger import get_logger
from page_loader.parser import process_resources

logger = get_logger(__name__)


def download(page_url: string, destination: string) -> string:
    if not Path(destination).exists():
        logger.error("destination folder %s doesn't exists", destination)
        raise RuntimeError("destination folder doesn't exists")

    content = load_url(page_url)

    progress = Progress()
    content = process_resources(content, page_url, destination, progress)

    file_path = get_page_download_path(page_url, destination)
    save_page(file_path, content)

    return str(file_path)
