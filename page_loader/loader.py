import string

import requests


def load_url(url: string) -> string:
    page = requests.get(url)
    return page.text


def load_url_content(url: string) -> string:
    page = requests.get(url)
    return page.content
