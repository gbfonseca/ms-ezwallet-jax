from ms_ezwallet_jax.src.infra.scraper.selenium import ScraperAdapter
from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions

scraper_adapter = ScraperAdapter()
get_actions = GetActions(scraper_adapter)

http_request = {
    'body': {
        'url': 'https://fundamentus.com.br/resultado.php'
    }
}

data = get_actions.handle(http_request)
print(data)
