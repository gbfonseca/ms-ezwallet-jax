from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions
from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.domain.usecases.add_actions import AddActions

mockReturn = [
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
    },
]


class ScraperStub(Scraper):

    def get_data(self, url: str):
        return [
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
            },
        ]


class AddActionsStub(AddActions):
    def add(self, data: list):
        fakeActionAdded = [
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
        return fakeActionAdded


def make_add_actions() -> AddActions:
    return AddActionsStub()


def make_scraper() -> Scraper:

    return ScraperStub()


def make_sut() -> GetActions:
    scraper_stub = make_scraper()
    add_actions_stub = make_add_actions()
    sut = GetActions(scraper_stub, add_actions_stub)
    return sut


def test_success_scrap(mocker):
    sut = make_sut()
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    response = sut.handle(http_request)

    assert response['status_code'] == 200
    assert response == {
        'status_code': 200,
        'body': mockReturn
    }


def test_get_actions_called_with_correct_value(mocker):
    # spy = mocker.patch(
    #     'tests.presentation.controllers.actions.get_actions_test.ScraperStub.get_data')
    spy = mocker.patch(
        'ms_ezwallet_jax.src.presentation.controllers.actions.get_actions.GetActions.handle')
    sut = make_sut()
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    response = sut.handle(http_request)

    # assert response['status_code'] == 500
    assert spy.called_with(http_request)
