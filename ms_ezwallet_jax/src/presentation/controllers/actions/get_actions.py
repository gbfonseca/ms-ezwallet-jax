from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.presentation.protocols.controller import Controller


class GetActions(Controller):
    def __init__(self, scraper: Scraper):
        self.scraper = scraper
        pass

    def handle(self, http_request):
        actions = self.scraper.get_data(http_request['body']['url'])
        return actions
