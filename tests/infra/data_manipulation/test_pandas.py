from ms_ezwallet_jax.src.infra.data_manipulation.pandas import DataManipulationAdapter
from tests.factories.html_string import html_string
from pytest_mock import MockFixture


def make_sut() -> DataManipulationAdapter:
    sut = DataManipulationAdapter()
    return sut


def test_should_return_a_list_of_dicts_on_success(mocker: MockFixture):
    sut = make_sut()

    data = html_string

    response = sut.to_dict(data)

    assert type(response) == list


def test_should_calls_DataManipulationAdapter_with_correct_value(mocker: MockFixture):
    sut = make_sut()
    spy = mocker.spy(sut, 'to_dict')

    data = html_string

    sut.to_dict(data)

    spy.assert_called_with(data)


def test_should_data_param_is_string(mocker: MockFixture):
    sut = make_sut()
    data = html_string

    sut.to_dict(data)

    assert type(data) == str
