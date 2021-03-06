from pytest_mock import MockFixture
from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from tests.factories.html_string import html_string
URL = 'https://fundamentus.com.br/resultado.php'


class ScraperAdapterStub(Scraper):
    def get_data(sef, url: str):
        return html_string


def make_sut() -> Scraper:
    return ScraperAdapterStub()


def test_ensure_return_a_html_content_on_success(mocker: MockFixture):
    sut = make_sut()

    response = sut.get_data(URL)

    assert response == html_string


def test_ensure_calls_get_data_with_correct_value(mocker: MockFixture):
    sut = make_sut()
    spy = mocker.spy(sut, 'get_data')
    sut.get_data(URL)

    spy.assert_called_with(URL)
