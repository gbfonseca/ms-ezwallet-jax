from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions
from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper

mockReturn = [
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


def make_scraper() -> Scraper:
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

    return ScraperStub()


def make_sut():
    scraper_stub = make_scraper()
    return GetActions(scraper_stub)


def test_param(mocker):
    sut = make_sut()
    spy = mocker.spy(sut, 'handle')
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    response = sut.handle(http_request)

    assert response == mockReturn
