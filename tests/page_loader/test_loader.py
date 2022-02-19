import tempfile
from pathlib import Path

import requests_mock

from page_loader import download
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


def test_download_page_with_multiple_sources():
    with requests_mock.Mocker() as m:
        content_mock = read_fixtures_file('multiple_resources.txt')
        url = 'https://ru.hexlet.io/courses'
        m.get(requests_mock.ANY, text='')
        m.get(url, text=content_mock)
        resources = [
            'ru-hexlet-io-courses_files/ru-hexlet-io-assets-application.css',
            'ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png',
            'ru-hexlet-io-courses_files/ru-hexlet-io-packs-js-runtime.js',
        ]

        with tempfile.TemporaryDirectory() as out_dict:
            expected_path = str(Path(out_dict).joinpath('ru-hexlet-io-courses.html').absolute())

            actual_path = download(url, out_dict)
            actual_content = read_file(actual_path)

            assert actual_path == expected_path
            for resource in resources:
                assert (resource in actual_content)
                assert Path(out_dict).joinpath(resource).exists()


