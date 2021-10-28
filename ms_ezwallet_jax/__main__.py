from ms_ezwallet_jax.src.infra.scraper.selenium import ScraperAdapter
from ms_ezwallet_jax.src.infra.html_parser.beautifulsoup import BeautifulSoupAdapter
from ms_ezwallet_jax.src.infra.data_manipulation.pandas import DataManipulationAdapter
from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions

beautifulsoup_adapter = BeautifulSoupAdapter()
data_manipulation_adapter = DataManipulationAdapter()
scraper_adapter = ScraperAdapter(
    beautifulsoup_adapter, data_manipulation_adapter)
get_actions = GetActions(scraper_adapter)

http_request = {
    'body': {
        'url': 'https://fundamentus.com.br/resultado.php'
    }
}

data = get_actions.handle(http_request)
print(data)
