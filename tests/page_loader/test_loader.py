import tempfile

import requests_mock

from page_loader.download import parse_local_image_links, save_images
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


def test_parse_image_links():
    content = read_fixtures_file('file_with_image_links1.html')
    actual_links = parse_local_image_links(content, 'https://test.ru')
    expected = {
        '/assets/professions/nodejs.png': 'https://test.ru/assets/professions/nodejs.png',
        'http://test.ru/assets/professions/some_image.png?t=5': 'http://test.ru/assets/professions/some_image.png'
    }

    assert actual_links == expected


def test_save_images():
    image_links = {
        '/assets/professions/nodejs.png': 'https://test.ru/assets/professions/nodejs.png',
        'http://test.ru/assets/professions/some_image.png?t=5': 'http://test.ru/assets/professions/some_image.png'
    }
    expected_image_content = b'1'

    with requests_mock.Mocker() as r_mock:
        r_mock.get(requests_mock.ANY, content=b'1')
        with tempfile.TemporaryDirectory() as out_dict:
            images_map = save_images(image_links, Path(out_dict))
            for image in image_links:
                image_downloaded_path = Path(out_dict).joinpath(images_map[image])
                actual_image = read_binary_file(image_downloaded_path.absolute())

                assert image in images_map
                assert image_downloaded_path.exists()
                assert expected_image_content == actual_image
