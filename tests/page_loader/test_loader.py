import tempfile

import pytest
import requests_mock

from page_loader.download import download_image
from page_loader import download
from pathlib import Path

from tests.file_loader import read_fixtures_file, read_file, read_binary_file


def test_download():
    with requests_mock.Mocker() as m:
        expected_content = read_fixtures_file('simple_page.txt')
        url = 'https://example.test'
        m.get(url, text=expected_content)

        with tempfile.TemporaryDirectory() as out_dict:
            expected_path = str(Path(out_dict).joinpath('example-test.html').absolute())

            actual_path = download(url, out_dict)
            actual_content = read_file(actual_path)

            assert actual_path == expected_path
            assert actual_content == expected_content


@pytest.mark.parametrize(
    ('url', 'expected_path'),
    [
        ('https://test.ru/assets/professions/nodejs.png', 'test-ru-assets-professions-nodejs.png'),
        ('http://test.ru/assets/professions/some_image.png', 'test-ru-assets-professions-some_image.png')
    ],
)
def test_download_image(url, expected_path):
    expected_image_content = b'1'

    with requests_mock.Mocker() as r_mock:
        r_mock.get(requests_mock.ANY, content=b'1')
        with tempfile.TemporaryDirectory() as out_dict:
            actual_path = download_image(url, Path(out_dict))
            image_downloaded_path = Path(out_dict).joinpath(expected_path)
            actual_image = read_binary_file(image_downloaded_path.absolute())

            assert actual_path == expected_path
            assert image_downloaded_path.exists()
            assert expected_image_content == actual_image
