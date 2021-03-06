import tempfile
from pathlib import Path

import pytest
import requests_mock

from page_loader.parser import download_and_save_resource, get_site_url
from tests.file_loader import read_binary_file


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
            actual_path = download_and_save_resource(url, Path(out_dict))
            image_downloaded_path = Path(out_dict).joinpath(expected_path)
            actual_image = read_binary_file(image_downloaded_path.absolute())

            assert actual_path == expected_path
            assert image_downloaded_path.exists()
            assert expected_image_content == actual_image


def test_get_site_url():
    assert get_site_url('http://example.com') == 'http://example.com'
    assert get_site_url('http://example.com/') == 'http://example.com'
    assert get_site_url('https://example.com/') == 'https://example.com'
    assert get_site_url('https://example.com?dsfds=5') == 'https://example.com'
    assert get_site_url('http://example.com/sdgdfgdfg') == 'http://example.com'
