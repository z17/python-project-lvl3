import string
from pathlib import Path

from page_loader.name_converter import convert_name


def get_page_download_path(page_url: string, destination: string) -> Path:
    name = convert_name(page_url)
    file_path = Path(destination).joinpath(name + '.html')
    return file_path


def get_resources_download_path(page_url: string, destination: string) -> Path:
    name = convert_name(page_url)
    resources_path = Path(destination).joinpath(name + '_files')
    return resources_path
