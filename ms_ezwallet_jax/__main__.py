from ms_ezwallet_jax.src.infra.scraper.selenium import ScraperAdapter
from ms_ezwallet_jax.src.infra.html_parser.beautifulsoup import BeautifulSoupAdapter
from ms_ezwallet_jax.src.infra.data_manipulation.pandas import DataManipulationAdapter
from ms_ezwallet_jax.src.presentation.controllers.actions.get_actions import GetActions
from ms_ezwallet_jax.src.infra.db.mongodb.repositories.actions.actions import ActionsRepository
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper
from ms_ezwallet_jax.src.data.usecases.db_add_actions_adapter import DbAddActionsAdapter

beautifulsoup_adapter = BeautifulSoupAdapter()
data_manipulation_adapter = DataManipulationAdapter()

scraper_adapter = ScraperAdapter(
    beautifulsoup_adapter, data_manipulation_adapter)
actions_repository = ActionsRepository()
db_add_actions_adapter = DbAddActionsAdapter(actions_repository)
get_actions = GetActions(scraper_adapter, db_add_actions_adapter)

http_request = {
    'body': {
        'url': 'https://fundamentus.com.br/resultado.php'
    }
}


mongo_helper.connect('mongodb://localhost:27017')

data = get_actions.handle(http_request)
