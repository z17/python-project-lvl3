import os
import string
import re
from urllib.parse import urlparse


def convert_name(url: string) -> string:
    name, parsed_url = convert_base(url)

    return name


def convert_resource_name(url: string) -> string:
    name, parsed_url = convert_base(url)
    extension = os.path.splitext(parsed_url.path)[1]
    extension = extension if extension else '.html'

    return name + extension


def convert_base(url: string):
    parsed_url = urlparse(url)

    path = parsed_url.path
    path = re.sub(r'\.\w{2,4}', '', path)

    query = parsed_url.query
    if query:
        query = '-' + query

    if path == '/':
        path = ''

    name = parsed_url.netloc + path + query
    name = re.sub(r'\W', '-', name)
    return name, parsed_url
