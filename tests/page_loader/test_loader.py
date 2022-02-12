import tempfile

import requests_mock

from page_loader.loader import convert_name
from page_loader import download
from pathlib import Path

from tests.file_loader import read_fixtures_file, read_file


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


# noinspection HttpUrlsUsage
def test_convert_name():
    assert convert_name('http://example.com') == 'example-com.html'
    assert convert_name('https://example.com') == 'example-com.html'
    assert convert_name('https://example.com/sdfdsf') == 'example-com-sdfdsf.html'
    assert convert_name('https://example.com/path1/path2.txt') == 'example-com-path1-path2.html'
    assert convert_name('https://example.com/path3?page=5') == 'example-com-path3-page-5.html'
