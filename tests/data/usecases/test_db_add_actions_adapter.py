from ms_ezwallet_jax.src.data.usecases.db_add_actions_adapter import DbAddActionsAdapter
from ms_ezwallet_jax.src.data.protocols.add_actions_repository import AddActionsRepository
from pytest_mock import MockFixture


def make_add_actions_repository() -> AddActionsRepository:
    class AddActionsRepositoryStub(AddActionsRepository):
        def add(self, data: list):
            return [
                {
                    "_id": 'any_id',
                    "Papel": "BBAS3",
                    "Cotação": 2917,
                    "P/L": 526,
                    "P/VP": "062",
                    "PSR": "0000",
                    "Div.Yield": "6,88%",
                    "P/Ativo": 0,
                    "P/Cap.Giro": "000",
                    "P/EBIT": "000",
                    "P/Ativ Circ.Liq": 0,
                    "EV/EBIT": "000",
                    "EV/EBITDA": "000",
                    "Mrg Ebit": "0,00%",
                    "Mrg. Líq.": "0,00%",
                    "Liq. Corr.": 0,
                    "ROIC": "0,00%",
                    "ROE": "11,73%",
                    "Liq.2meses": "419.635.000,00",
                    "Patrim. Líq": "135.444.000.000,00",
                    "Dív.Brut/ Patrim.": "000",
                    "Cresc. Rec.5a": "0,79%"
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
            "Papel": "BBAS3",
            "Cotação": 2917,
            "P/L": 526,
            "P/VP": "062",
            "PSR": "0000",
            "Div.Yield": "6,88%",
            "P/Ativo": 0,
            "P/Cap.Giro": "000",
            "P/EBIT": "000",
            "P/Ativ Circ.Liq": 0,
            "EV/EBIT": "000",
            "EV/EBITDA": "000",
            "Mrg Ebit": "0,00%",
            "Mrg. Líq.": "0,00%",
            "Liq. Corr.": 0,
            "ROIC": "0,00%",
            "ROE": "11,73%",
            "Liq.2meses": "419.635.000,00",
            "Patrim. Líq": "135.444.000.000,00",
            "Dív.Brut/ Patrim.": "000",
            "Cresc. Rec.5a": "0,79%"
        }
    ]

    response = sut.add(data)

    assert response == [
        {
            "_id": 'any_id',
            "Papel": "BBAS3",
            "Cotação": 2917,
            "P/L": 526,
            "P/VP": "062",
            "PSR": "0000",
            "Div.Yield": "6,88%",
            "P/Ativo": 0,
            "P/Cap.Giro": "000",
            "P/EBIT": "000",
            "P/Ativ Circ.Liq": 0,
            "EV/EBIT": "000",
            "EV/EBITDA": "000",
            "Mrg Ebit": "0,00%",
            "Mrg. Líq.": "0,00%",
            "Liq. Corr.": 0,
            "ROIC": "0,00%",
            "ROE": "11,73%",
            "Liq.2meses": "419.635.000,00",
            "Patrim. Líq": "135.444.000.000,00",
            "Dív.Brut/ Patrim.": "000",
            "Cresc. Rec.5a": "0,79%"
        }
    ]


def test_db_add_actions_adapter_calls_with_correct_values(mocker: MockFixture):
    [sut, add_actions_repository] = make_sut()
    spy = mocker.spy(add_actions_repository, 'add')
    data = [
        {
            "Papel": "BBAS3",
            "Cotação": 2917,
            "P/L": 526,
            "P/VP": "062",
            "PSR": "0000",
            "Div.Yield": "6,88%",
            "P/Ativo": 0,
            "P/Cap.Giro": "000",
            "P/EBIT": "000",
            "P/Ativ Circ.Liq": 0,
            "EV/EBIT": "000",
            "EV/EBITDA": "000",
            "Mrg Ebit": "0,00%",
            "Mrg. Líq.": "0,00%",
            "Liq. Corr.": 0,
            "ROIC": "0,00%",
            "ROE": "11,73%",
            "Liq.2meses": "419.635.000,00",
            "Patrim. Líq": "135.444.000.000,00",
            "Dív.Brut/ Patrim.": "000",
            "Cresc. Rec.5a": "0,79%"
        }
    ]

    response = sut.add(data)

    spy.assert_called_with(data)
