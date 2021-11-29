from ms_ezwallet_jax.src.data.usecases.db_add_actions_adapter import DbAddActionsAdapter
from ms_ezwallet_jax.src.data.protocols.add_actions_repository import AddActionsRepository
from pytest_mock import MockFixture


def make_add_actions_repository() -> AddActionsRepository:
    class AddActionsRepositoryStub(AddActionsRepository):
        def add(self, data: list):
            return [
                {
                    "_id": 'any_id',
                    "code": "BBAS3",
                }
            ]
    return AddActionsRepositoryStub()


def make_sut() -> [DbAddActionsAdapter, AddActionsRepository]:
    add_actions_repository_stub = make_add_actions_repository()
    sut = DbAddActionsAdapter(add_actions_repository_stub)
    return [sut, add_actions_repository_stub]


def test_db_add_actions_adapter_returns_an_actions_on_success(mocker: MockFixture):
    [sut, _] = make_sut()

    data = [
        {
            "code": "BBAS3",
        }
    ]

    response = sut.add(data)

    assert response == [
        {
            "_id": 'any_id',
            "code": "BBAS3",
        }
    ]


def test_db_add_actions_adapter_calls_add_with_correct_value(mocker: MockFixture):
    [sut, _] = make_sut()

    spy = mocker.spy(sut, 'add')

    data = [
        {
            "code": "BBAS3",
        }
    ]

    response = sut.add(data)

    spy.assert_called_with(data)


def test_db_add_actions_adapter_calls_with_correct_values(mocker: MockFixture):
    [sut, add_actions_repository] = make_sut()
    spy = mocker.spy(add_actions_repository, 'add')
    data = [
        {
            "code": "BBAS3",
        }
    ]

    response = sut.add(data)

    spy.assert_called_with(data)


def test_db_add_actions_adapter_returns_item_action_with_id(mocker: MockFixture):
    [sut, _] = make_sut()

    data = [
        {
            "code": "BBAS3",
        }
    ]

    response = sut.add(data)

    for action in response:
        assert action['_id']
