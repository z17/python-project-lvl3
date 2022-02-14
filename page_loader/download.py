import string
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.loader import load_url, load_image_url
from page_loader.name_converter import convert_name, convert_image_name, get_site_url


def download(page_url: string, destination: string) -> string:
    site_url = get_site_url(page_url)
    name = convert_name(page_url)
    content = load_url(page_url)

    file_path = Path(destination).joinpath(name + '.html')
    resources_path = Path(destination).joinpath(name + '_files')
    if not resources_path.exists():
        resources_path.mkdir(parents=True)

    content = replace_images(content, site_url, resources_path)

    with file_path.open('w') as file:
        file.write(content)

    return str(file_path)


def replace_images(page_content: string, site_url: string, resources_folder: Path) -> string:
    parsed_domain = urlparse(site_url)
    soup = BeautifulSoup(page_content, 'html.parser')
    for img in soup.find_all('img'):
        image_url = img.get('src')
        parsed_url = urlparse(image_url)

        full_url = ''
        if not parsed_url.netloc:
            full_url = '{site_url}{image_url}'.format(site_url=site_url, image_url=parsed_url.path)

        if parsed_url.netloc == parsed_domain.netloc:
            full_url = '{url.scheme}://{url.netloc}{url.path}'.format(url=parsed_url)

        if not full_url:
            continue

        image_location = download_image(full_url, resources_folder)
        img['src'] = str(Path(resources_folder.name).joinpath(image_location))

    return soup.prettify()


def download_image(url: string, folder: Path) -> string:
    image_data = load_image_url(url)
    image_name = convert_image_name(url)
    image_path = folder.joinpath(image_name)
    with open(image_path, 'wb') as handler:
        handler.write(image_data)
    return image_name
