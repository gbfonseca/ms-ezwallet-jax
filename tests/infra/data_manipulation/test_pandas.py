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
