from pytest_mock import MockFixture
from ms_ezwallet_jax.src.presentation.controllers.actions.get_action_data_by_code import GetActionDataByCodeController


def make_sut() -> GetActionDataByCodeController:
    sut = GetActionDataByCodeController()
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
