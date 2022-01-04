from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.domain.usecases.add_actions import AddActions
from ms_ezwallet_jax.src.presentation.protocols.controller import Controller
from ms_ezwallet_jax.src.presentation.protocols.http import HttpResponse
from ms_ezwallet_jax.src.presentation.helpers.http import ok, server_error
from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation


class GetActions(Controller):
    def __init__(self, data_manipulation: DataManipulation, add_actions: AddActions):
        self.data_manipulation = data_manipulation
        self.add_actions = add_actions

    def handle(self, http_request) -> HttpResponse:
        try:

            actions = self.data_manipulation.to_dict('')
            savedActions = self.add_actions.add(actions)
            return ok(savedActions)
        except:
            return server_error()
