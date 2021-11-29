from ms_ezwallet_jax.src.presentation.protocols.controller import Controller
from ms_ezwallet_jax.src.presentation.protocols.http import HttpRequest, HttpResponse
from ms_ezwallet_jax.src.presentation.helpers.http import ok, server_error, bad_request


class GetActionDataByCodeController(Controller):
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            if (http_request['params'] is None or http_request['params']['code'] is None):
                return bad_request('Código obrigatório.')

            return
        except:
            return server_error()
