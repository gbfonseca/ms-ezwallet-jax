from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.domain.usecases.add_actions import AddActions
from ms_ezwallet_jax.src.presentation.protocols.controller import Controller


class GetActions(Controller):
    def __init__(self, scraper: Scraper, add_actions: AddActions):
        self.scraper = scraper
        self.add_actions = add_actions

    def handle(self, http_request):
        actions = self.scraper.get_data(http_request['body']['url'])
        savedActions = self.add_actions.add(actions)
        return savedActions
