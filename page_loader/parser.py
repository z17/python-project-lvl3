import string
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.file_paths import get_resources_download_path
from page_loader.file_saver import save_resource
from page_loader.loader import load_url_content
from page_loader.logger import get_logger
from page_loader.name_converter import convert_resource_name, get_site_url
from page_loader.Progress import Progress

ALLOWED_TAGS = ('img', 'link', 'script')
TAGS_LINK_ATTRIBUTES = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}

logger = get_logger(__name__)


def process_resources(page_content: string, page_url: string, destination: string, progress: Progress) -> string:
    resources_path = get_resources_download_path(page_url, destination)
    if not resources_path.exists():
        resources_path.mkdir(parents=True)
        logger.info("resource output folder created - %s", str(resources_path))

    site_url = get_site_url(page_url)

    parsed_domain = urlparse(site_url)
    soup = BeautifulSoup(page_content, 'html.parser')
    tags = soup.find_all(ALLOWED_TAGS)
    progress.processing_resources_start(len(tags))
    for tag in tags:
        progress.processing_resources_next()
        tag_name = TAGS_LINK_ATTRIBUTES[tag.name]
        url = tag.get(tag_name)
        if not url:
            continue

        parsed_url = urlparse(url)

        full_url = ''
        if not parsed_url.netloc:
            full_url = '{site_url}{image_url}'.format(site_url=site_url, image_url=parsed_url.path)

        if parsed_url.netloc == parsed_domain.netloc:
            url_schema = parsed_url.scheme if parsed_url.scheme else parsed_domain.scheme
            full_url = '{url_schema}://{url.netloc}{url.path}'.format(url=parsed_url, url_schema=url_schema)

        if not full_url:
            continue

        resource_location = download_and_save_resource(full_url, resources_path)
        tag[tag_name] = resources_path.name + '/' + resource_location

    progress.processing_resources_finish()

    return soup.prettify()


def download_and_save_resource(url: string, folder: Path) -> string:
    data = load_url_content(url)
    name = convert_resource_name(url)
    path = folder.joinpath(name)
    save_resource(path, data)
    return name
