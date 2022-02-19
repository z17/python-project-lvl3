import string
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from loader import load_url_content
from name_converter import convert_resource_name

TAGS_LINK_ATTRIBUTES = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def replace_resources(page_content: string, site_url: string, resources_folder: Path) -> string:
    allowed_tags = ('img', 'link', 'script')
    parsed_domain = urlparse(site_url)
    soup = BeautifulSoup(page_content, 'html.parser')
    for tag in soup.find_all(allowed_tags):
        tag_name = TAGS_LINK_ATTRIBUTES[tag.name]
        url = tag.get(tag_name)
        if not url:
            continue
        parsed_url = urlparse(url)

        full_url = ''
        if not parsed_url.netloc:
            full_url = '{site_url}{image_url}'.format(site_url=site_url, image_url=parsed_url.path)

        if parsed_url.netloc == parsed_domain.netloc:
            full_url = '{url.scheme}://{url.netloc}{url.path}'.format(url=parsed_url)

        if not full_url:
            continue

        resource_location = download_resource(full_url, resources_folder)
        tag[tag_name] = resources_folder.name + '/' + resource_location

    return soup.prettify()


def download_resource(url: string, folder: Path) -> string:
    data = load_url_content(url)
    name = convert_resource_name(url)
    path = folder.joinpath(name)
    with open(path, 'wb') as handler:
        handler.write(data)
    return name
