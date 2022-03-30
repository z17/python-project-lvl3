import pytest

from page_loader.name_converter import convert_name, get_site_url, convert_resource_name


# noinspection HttpUrlsUsage
@pytest.mark.parametrize(
    ('url', 'expected_name'),
    [
        ('http://example.com', 'example-com'),
        ('https://example.com', 'example-com'),
        ('http://example.com/', 'example-com'),
        ('https://example.com/sdfdsf', 'example-com-sdfdsf'),
        ('https://example.com/path1/path2.txt', 'example-com-path1-path2'),
        ('https://example.com/path3?page=5', 'example-com-path3-page-5'),
    ],
)
def test_convert_name(url, expected_name):
    assert convert_name(url) == expected_name


# noinspection HttpUrlsUsage
@pytest.mark.parametrize(
    ('url', 'expected_name'),
    [
        ('https://ru.hexlet.io/assets/application.css',
         'ru-hexlet-io-assets-application.css'),
        ('https://ru.hexlet.io/assets_application.js',
         'ru-hexlet-io-assets_application.js'),
        ('http://example.com/test/page',
         'example-com-test-page.html'),
        ('http://example.com/test/page.htm',
         'example-com-test-page.htm'),
    ],
)
def test_convert_resource_name(url, expected_name):
    actual_name = convert_resource_name(url)
    assert actual_name == expected_name


def test_get_site_url():
    assert get_site_url('http://example.com') == 'http://example.com'
    assert get_site_url('http://example.com/') == 'http://example.com'
    assert get_site_url('https://example.com/') == 'https://example.com'
    assert get_site_url('https://example.com?dsfds=5') == 'https://example.com'
    assert get_site_url('http://example.com/sdgdfgdfg') == 'http://example.com'
