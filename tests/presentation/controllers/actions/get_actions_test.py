from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions
from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.domain.usecases.add_actions import AddActions
from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation

from pytest_mock import MockFixture


class DataManipulationStub(DataManipulation):
    def to_dict(self, data: str):
        return [
            {
                'code': 'BBAS3'
            }
        ]


class AddActionsStub(AddActions):
    def add(self, data: list):
        fakeActionAdded = [
            {
                "_id": 'any_id',
                "code": "BBAS3",
            }
        ]
        return fakeActionAdded


def make_data_manipulation() -> DataManipulation:
    return DataManipulationStub()


def make_add_actions() -> AddActions:
    return AddActionsStub()


def make_sut() -> [GetActions,  Scraper, HtmlParser, DataManipulation, AddActions]:
    data_manipulation_stub = make_data_manipulation()
    add_actions_stub = make_add_actions()
    sut = GetActions(
        data_manipulation_stub, add_actions_stub)
    return [sut, data_manipulation_stub, add_actions_stub]


def test_success_scrap(mocker: MockFixture):
    [sut, _, _] = make_sut()
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    response = sut.handle(http_request)

    assert response['status_code'] == 200
    assert response == {
        'status_code': 200,
        'body': [
            {
                "_id": 'any_id',
                "code": "BBAS3",
            },
        ]
    }


def test_get_actions_called_with_correct_value(mocker: MockFixture):
    [sut, _, _] = make_sut()
    spy = mocker.spy(sut, 'handle')
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    response = sut.handle(http_request)

    spy.assert_called_with(http_request)


def test_get_actions_return_if_data_manipulation_throws(mocker: MockFixture):
    [sut, data_manipulation_stub, _] = make_sut()
    spy = mocker.spy(data_manipulation_stub, 'to_dict')
    spy.side_effect = Exception()
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    http_response = sut.handle(http_request)

    assert http_response['status_code'] == 500


def test_get_actions_return_500_if_add_actions_throws(mocker: MockFixture):
    [sut, _, add_actions_stub] = make_sut()
    spy = mocker.spy(add_actions_stub, 'add')
    spy.side_effect = Exception()
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    http_response = sut.handle(http_request)

    assert http_response['status_code'] == 500


def test_add_actions_return_an_actions_on_success(mocker: MockFixture):
    [sut, _, add_actions_stub] = make_sut()
    spy = mocker.spy(add_actions_stub, 'add')
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    sut.handle(http_request)

    assert spy.spy_return == [
        {
            "_id": "any_id",
            "code": "BBAS3",
        }
    ]
