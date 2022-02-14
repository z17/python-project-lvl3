import string
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from loader import load_url, load_image_url
from name_converter import convert_name, convert_image_name


def download(page_url: string, destination: string) -> string:
    site_url = ''  # todo
    name = convert_name(page_url)
    content = load_url(page_url)

    file_path = Path(destination).joinpath(name + '.html')
    resources_path = Path(destination).joinpath(name + '_files')

    image_links = parse_local_image_links(content, site_url)

    image_links_map = save_images(image_links, resources_path)

    content = replace_images(content, image_links_map)

    with file_path.open('w') as file:
        file.write(content)

    return str(file_path)


def parse_local_image_links(page_content: string, site_url: string) -> dict[string, string]:
    parsed_domain = urlparse(site_url)
    soup = BeautifulSoup(page_content, 'html.parser')
    images = {}
    for img in soup.find_all('img'):
        image_url = img.get('src')
        parsed_url = urlparse(image_url)
        if not parsed_url.netloc:
            full_url = '{site_url}{image_url}'.format(site_url=site_url, image_url=parsed_url.path)
            images[image_url] = full_url

        if parsed_url.netloc == parsed_domain.netloc:
            full_url = '{url.scheme}://{url.netloc}{url.path}'.format(url=parsed_url)
            images[image_url] = full_url

    return images


def save_images(image_links: dict[string, string], folder: Path) -> dict[string, string]:
    result = {}
    for image in image_links:
        full_image_url = image_links[image]
        image_data = load_image_url(full_image_url)
        image_name = convert_image_name(full_image_url)
        image_path = folder.joinpath(image_name)
        with open(image_path, 'wb') as handler:
            handler.write(image_data)
        result[image] = image_name

    return result


def replace_images(content: string, image_links_map: dict[string, string]) -> string:
    # todo
    return content
