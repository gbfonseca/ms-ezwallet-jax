from src.presentation.controllers.actions.get_actions import GetActions
from pytest_mock import mocker


def make_sut():
    return GetActions()


def test_param(mocker: mocker):
    m = mocker.Mocker()
    sut = make_sut()
    spy = mocker.spy(sut, 'handle')
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    sut.handle(http_request)

    assert spy.assert_called_with(http_request)
