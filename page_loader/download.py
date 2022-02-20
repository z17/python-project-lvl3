import string
from pathlib import Path

from page_loader.loader import load_url
from page_loader.name_converter import convert_name, get_site_url
from page_loader.parser import replace_resources


def download(page_url: string, destination: string) -> string:
    site_url = get_site_url(page_url)
    name = convert_name(page_url)
    content = load_url(page_url)

    file_path = Path(destination).joinpath(name + '.html')
    resources_path = Path(destination).joinpath(name + '_files')
    if not resources_path.exists():
        resources_path.mkdir(parents=True)

    content = replace_resources(content, site_url, resources_path)

    with file_path.open('w') as file:
        file.write(content)

    return str(file_path)
