from pytest_mock import MockFixture
from ms_ezwallet_jax.src.presentation.controllers.actions.get_action_data_by_code import GetActionDataByCodeController
from ms_ezwallet_jax.src.domain.usecases.http_client import HttpClient
from tests.factories.action import action


class HttpClientStub(HttpClient):
    def get(self, url: str):
        return action


def make_http_client() -> HttpClient:
    return HttpClientStub()


def make_sut() -> GetActionDataByCodeController:
    http_client_stub = make_http_client()
    sut = GetActionDataByCodeController(http_client_stub)
    return sut


def test_should_return_400_if_code_not_provided(mocker: MockFixture):
    sut = make_sut()

    http_request = {
        'params': {
            'code': None
        }
    }
    response = sut.handle(http_request)
    assert response['status_code'] == 400
    assert response['body']['message'] == 'Código obrigatório.'


def test_should_return_200_on_success(mocker: MockFixture):
    sut = make_sut()

    http_request = {
        'params': {
            'code': 'bbas3.sa'
        }
    }
    response = sut.handle(http_request)

    assert response['status_code'] == 200
