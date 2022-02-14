import string
from pathlib import Path


def read_fixtures_file(name: string) -> string:
    file = str(Path(__file__)
               .parent
               .joinpath('fixtures')
               .joinpath(name)
               .absolute())
    with open(file, 'r') as file:
        return file.read()


def read_file(file_path: string) -> string:
    with open(file_path, 'r') as file:
        return file.read()


def read_binary_file(file_path: string) -> string:
    with open(file_path, 'rb') as file:
        return file.read()
