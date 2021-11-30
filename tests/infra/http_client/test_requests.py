from pytest_mock import MockFixture
from ms_ezwallet_jax.src.infra.http_client.requests import RequestsAdapter
from ms_ezwallet_jax.src.domain.usecases.http_client import HttpClient

FAKE_URL = 'https://any_url.com'


def make_sut() -> HttpClient:
    return RequestsAdapter()


def test_should_return_an_exception_if_no_url_provided(mocker: MockFixture):
    sut = make_sut()
    URL = None
    response = sut.get(URL)

    assert type(response) == Exception
