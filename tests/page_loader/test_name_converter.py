from page_loader.name_converter import convert_name, get_site_url


# noinspection HttpUrlsUsage
def test_convert_name():
    assert convert_name('http://example.com') == 'example-com'
    assert convert_name('https://example.com') == 'example-com'
    assert convert_name('http://example.com/') == 'example-com'
    assert convert_name('https://example.com/sdfdsf') == 'example-com-sdfdsf'
    assert convert_name('https://example.com/path1/path2.txt') == 'example-com-path1-path2'
    assert convert_name('https://example.com/path3?page=5') == 'example-com-path3-page-5'


def test_get_site_url():
    assert get_site_url('http://example.com') == 'http://example.com'
    assert get_site_url('http://example.com/') == 'http://example.com'
    assert get_site_url('https://example.com/') == 'https://example.com'
    assert get_site_url('https://example.com?dsfds=5') == 'https://example.com'
    assert get_site_url('http://example.com/sdgdfgdfg') == 'http://example.com'
