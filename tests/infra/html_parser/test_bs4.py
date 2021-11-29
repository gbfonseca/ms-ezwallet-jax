from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions
from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from tests.factories.html_string import html_string
from tests.factories.parsed_html_string import parsed_html_string

from pytest_mock import MockFixture


class HtmlParserStub(HtmlParser):
    def parse_html(self, html_content: str) -> str:
        return parsed_html_string


def make_sut() -> HtmlParser:
    return HtmlParserStub()


def test_return_a_parsed_html_string_on_success(mocker: MockFixture):
    sut = make_sut()

    response = sut.parse_html(html_string)
    assert type(response) == str
