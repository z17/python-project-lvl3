import string
import re
from urllib.parse import urlparse
from pathlib import Path

import requests


def download(url: string, destination: string) -> string:
    name = convert_name(url)
    page = requests.get(url)
    content = page.text
    file_path = Path(destination).joinpath(name)

    with file_path.open('w') as file:
        file.write(content)

    return str(file_path)


def convert_name(url: string) -> string:
    parsed_url = urlparse(url)

    path = parsed_url.path
    path = re.sub(r'\.\w{2,4}', '', path)

    query = parsed_url.query
    if query:
        query = '-' + query

    name = parsed_url.netloc + path + query
    name = re.sub(r'\W', '-', name)
    name = name + '.html'

    return name
