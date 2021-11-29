from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions
from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.domain.usecases.add_actions import AddActions
from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation

from pytest_mock import MockFixture


class ScraperStub(Scraper):

    def get_data(self, url: str):
        return """
        <table>
        <thead>
        <tr>
        <th style="-moz-user-select: none;" class="fd-column-0 sortable-text "><a href="#" class="fdTableSortTrigger" title="Sort on “Papel”">Papel</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-1"><a href="#" class="fdTableSortTrigger" title="Sort on “Cotação”">Cotação</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-2"><a href="#" class="fdTableSortTrigger" title="Sort on “P/L”">P/L</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-3"><a href="#" class="fdTableSortTrigger" title="Sort on “P/VP”">P/VP</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-4"><a href="#" class="fdTableSortTrigger" title="Sort on “PSR”">PSR</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-5"><a href="#" class="fdTableSortTrigger" title="Sort on “Div.Yield”">Div.Yield</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-6"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Ativo”">P/Ativo</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-7"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Cap.Giro”">P/Cap.Giro</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-8"><a href="#" class="fdTableSortTrigger" title="Sort on “P/EBIT”">P/EBIT</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-9"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Ativ Circ.Liq”">P/Ativ Circ.Liq</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-10"><a href="#" class="fdTableSortTrigger" title="Sort on “EV/EBIT”">EV/EBIT</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-11"><a href="#" class="fdTableSortTrigger" title="Sort on “EV/EBITDA”">EV/EBITDA</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-12"><a href="#" class="fdTableSortTrigger" title="Sort on “Mrg Ebit”">Mrg Ebit</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-13"><a href="#" class="fdTableSortTrigger" title="Sort on “Mrg. Líq.”">Mrg. Líq.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-14"><a href="#" class="fdTableSortTrigger" title="Sort on “Liq. Corr.”">Liq. Corr.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-15"><a href="#" class="fdTableSortTrigger" title="Sort on “ROIC”">ROIC</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-16"><a href="#" class="fdTableSortTrigger" title="Sort on “ROE”">ROE</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-17"><a href="#" class="fdTableSortTrigger" title="Sort on “Liq.2meses”">Liq.2meses</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-18"><a href="#" class="fdTableSortTrigger" title="Sort on “Patrim. Líq”">Patrim. Líq</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-19"><a href="#" class="fdTableSortTrigger" title="Sort on “Dív.Brut/ Patrim.”">Dív.Brut/ Patrim.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-20"><a href="#" class="fdTableSortTrigger" title="Sort on “Cresc. Rec.5a”">Cresc. Rec.5a</a></th>
        </tr>
        <thead>
        <tbody>
        <tr class="">
        <td ckass="res_papel"><span class="tips"><a href="detalhes.php?papel=BBAS3">BBAS3</a></span></td>
        <td>27,03</td>
        <td>70,36</td>
        <td>1,34</td>
        <td>0,920</td>
        <td>0,00%</td>
        <td>0,636</td>
        <td>8,60</td>
        <td>17,97</td>
        <td>-2,72</td>
        <td>21,51</td>
        <td>9,29</td>
        <td>5,12%</td>
        <td>1,29%</td>
        <td>1,34</td>
        <td>4,42%</td>
        <td>1,90%</td>
        <td>385.268.000,00</td>
        <td>27.849.900.000,00</td>
        <td>0,46</td>
        <td>2,92%</td>
        </tr>
        </tbody>
        </table>
        """


class HtmlParserStub(HtmlParser):
    def parse_html(self, html_content: str) -> str:
        return """
        <table>
        <thead>
        <tr>
        <th style="-moz-user-select: none;" class="fd-column-0 sortable-text "><a href="#" class="fdTableSortTrigger" title="Sort on “Papel”">Papel</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-1"><a href="#" class="fdTableSortTrigger" title="Sort on “Cotação”">Cotação</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-2"><a href="#" class="fdTableSortTrigger" title="Sort on “P/L”">P/L</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-3"><a href="#" class="fdTableSortTrigger" title="Sort on “P/VP”">P/VP</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-4"><a href="#" class="fdTableSortTrigger" title="Sort on “PSR”">PSR</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-5"><a href="#" class="fdTableSortTrigger" title="Sort on “Div.Yield”">Div.Yield</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-6"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Ativo”">P/Ativo</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-7"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Cap.Giro”">P/Cap.Giro</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-8"><a href="#" class="fdTableSortTrigger" title="Sort on “P/EBIT”">P/EBIT</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-9"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Ativ Circ.Liq”">P/Ativ Circ.Liq</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-10"><a href="#" class="fdTableSortTrigger" title="Sort on “EV/EBIT”">EV/EBIT</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-11"><a href="#" class="fdTableSortTrigger" title="Sort on “EV/EBITDA”">EV/EBITDA</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-12"><a href="#" class="fdTableSortTrigger" title="Sort on “Mrg Ebit”">Mrg Ebit</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-13"><a href="#" class="fdTableSortTrigger" title="Sort on “Mrg. Líq.”">Mrg. Líq.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-14"><a href="#" class="fdTableSortTrigger" title="Sort on “Liq. Corr.”">Liq. Corr.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-15"><a href="#" class="fdTableSortTrigger" title="Sort on “ROIC”">ROIC</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-16"><a href="#" class="fdTableSortTrigger" title="Sort on “ROE”">ROE</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-17"><a href="#" class="fdTableSortTrigger" title="Sort on “Liq.2meses”">Liq.2meses</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-18"><a href="#" class="fdTableSortTrigger" title="Sort on “Patrim. Líq”">Patrim. Líq</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-19"><a href="#" class="fdTableSortTrigger" title="Sort on “Dív.Brut/ Patrim.”">Dív.Brut/ Patrim.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-20"><a href="#" class="fdTableSortTrigger" title="Sort on “Cresc. Rec.5a”">Cresc. Rec.5a</a></th>
        </tr>
        <thead>
        <tbody>
        <tr class="">
        <td ckass="res_papel"><span class="tips"><a href="detalhes.php?papel=BBAS3">BBAS3</a></span></td>
        <td>27,03</td>
        <td>70,36</td>
        <td>1,34</td>
        <td>0,920</td>
        <td>0,00%</td>
        <td>0,636</td>
        <td>8,60</td>
        <td>17,97</td>
        <td>-2,72</td>
        <td>21,51</td>
        <td>9,29</td>
        <td>5,12%</td>
        <td>1,29%</td>
        <td>1,34</td>
        <td>4,42%</td>
        <td>1,90%</td>
        <td>385.268.000,00</td>
        <td>27.849.900.000,00</td>
        <td>0,46</td>
        <td>2,92%</td>
        </tr>
        </tbody>
        </table>
        """


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


def make_html_parser() -> HtmlParserStub:
    return HtmlParserStub()


def make_data_manipulation() -> DataManipulation:
    return DataManipulationStub()


def make_add_actions() -> AddActions:
    return AddActionsStub()


def make_scraper() -> Scraper:

    return ScraperStub()


def make_sut() -> [GetActions, Scraper, AddActions]:
    scraper_stub = make_scraper()
    html_parser_stub = make_html_parser()
    data_manipulation_stub = make_data_manipulation()
    add_actions_stub = make_add_actions()
    sut = GetActions(scraper_stub, html_parser_stub,
                     data_manipulation_stub, add_actions_stub)
    return [sut, scraper_stub, add_actions_stub]


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


def test_scraper_called_with_correct_value(mocker: MockFixture):
    [sut, scraper_stub, _] = make_sut()
    spy = mocker.spy(scraper_stub, 'get_data')
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    sut.handle(http_request)

    spy.assert_called_with(http_request['body']['url'])


def test_get_actions_return_500_if_scraper_throws(mocker: MockFixture):
    [sut, scraper_stub, _] = make_sut()
    spy = mocker.spy(scraper_stub, 'get_data')
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


def test_scraper_return_an_actions_on_success(mocker: MockFixture):
    [sut, scraper_stub, _] = make_sut()
    spy = mocker.spy(scraper_stub, 'get_data')
    http_request = {
        'body': {
            'url': 'https://fundamentus.com.br/resultado.php'
        }
    }

    sut.handle(http_request)

    assert spy.spy_return == """
        <table>
        <thead>
        <tr>
        <th style="-moz-user-select: none;" class="fd-column-0 sortable-text "><a href="#" class="fdTableSortTrigger" title="Sort on “Papel”">Papel</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-1"><a href="#" class="fdTableSortTrigger" title="Sort on “Cotação”">Cotação</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-2"><a href="#" class="fdTableSortTrigger" title="Sort on “P/L”">P/L</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-3"><a href="#" class="fdTableSortTrigger" title="Sort on “P/VP”">P/VP</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-4"><a href="#" class="fdTableSortTrigger" title="Sort on “PSR”">PSR</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-5"><a href="#" class="fdTableSortTrigger" title="Sort on “Div.Yield”">Div.Yield</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-6"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Ativo”">P/Ativo</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-7"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Cap.Giro”">P/Cap.Giro</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-8"><a href="#" class="fdTableSortTrigger" title="Sort on “P/EBIT”">P/EBIT</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-9"><a href="#" class="fdTableSortTrigger" title="Sort on “P/Ativ Circ.Liq”">P/Ativ Circ.Liq</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-10"><a href="#" class="fdTableSortTrigger" title="Sort on “EV/EBIT”">EV/EBIT</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-11"><a href="#" class="fdTableSortTrigger" title="Sort on “EV/EBITDA”">EV/EBITDA</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-12"><a href="#" class="fdTableSortTrigger" title="Sort on “Mrg Ebit”">Mrg Ebit</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-13"><a href="#" class="fdTableSortTrigger" title="Sort on “Mrg. Líq.”">Mrg. Líq.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-14"><a href="#" class="fdTableSortTrigger" title="Sort on “Liq. Corr.”">Liq. Corr.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-15"><a href="#" class="fdTableSortTrigger" title="Sort on “ROIC”">ROIC</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-16"><a href="#" class="fdTableSortTrigger" title="Sort on “ROE”">ROE</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-17"><a href="#" class="fdTableSortTrigger" title="Sort on “Liq.2meses”">Liq.2meses</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-18"><a href="#" class="fdTableSortTrigger" title="Sort on “Patrim. Líq”">Patrim. Líq</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-19"><a href="#" class="fdTableSortTrigger" title="Sort on “Dív.Brut/ Patrim.”">Dív.Brut/ Patrim.</a></th>
        <th style="-moz-user-select: none;" class="sortable-numeric fd-column-20"><a href="#" class="fdTableSortTrigger" title="Sort on “Cresc. Rec.5a”">Cresc. Rec.5a</a></th>
        </tr>
        <thead>
        <tbody>
        <tr class="">
        <td ckass="res_papel"><span class="tips"><a href="detalhes.php?papel=BBAS3">BBAS3</a></span></td>
        <td>27,03</td>
        <td>70,36</td>
        <td>1,34</td>
        <td>0,920</td>
        <td>0,00%</td>
        <td>0,636</td>
        <td>8,60</td>
        <td>17,97</td>
        <td>-2,72</td>
        <td>21,51</td>
        <td>9,29</td>
        <td>5,12%</td>
        <td>1,29%</td>
        <td>1,34</td>
        <td>4,42%</td>
        <td>1,90%</td>
        <td>385.268.000,00</td>
        <td>27.849.900.000,00</td>
        <td>0,46</td>
        <td>2,92%</td>
        </tr>
        </tbody>
        </table>
        """


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
