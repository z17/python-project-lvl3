import pytest
import requests_mock

from loader import load_url


def test_loader_errors():
    with pytest.raises(RuntimeError):
        load_url('https://asdfasdfa4234sf.ru')


def test_loader_error_status():
    url = 'https://example.com'
    with requests_mock.Mocker() as m:
        m.get(url, status_code=404)
        with pytest.raises(RuntimeError):
            load_url(url)
