from ms_ezwallet_jax.src.presentation.protocols.controller import Controller
from ms_ezwallet_jax.src.presentation.protocols.http import HttpRequest, HttpResponse
from ms_ezwallet_jax.src.presentation.helpers.http import ok, server_error, bad_request
from ms_ezwallet_jax.src.domain.usecases.http_client import HttpClient


class GetActionDataByCodeController(Controller):

    YF_URL = 'https://query2.finance.yahoo.com/v8/finance/chart'

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            if (http_request['params'] is None or http_request['params']['code'] is None):
                return bad_request('Código obrigatório.')
            code = http_request['params']['code']
            data = self.http_client.get(
                '{}/{}'.format(self.YF_URL, code))

            if(data['chart']['result'] is None):
                return bad_request('Código inválido.')

            return ok(data)
        except:
            return server_error()
