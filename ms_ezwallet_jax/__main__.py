from ms_ezwallet_jax.src.main.config.configuration import configuration
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper
from ms_ezwallet_jax.src.main.factories.get_actions import make_get_actions

get_actions = make_get_actions()

http_request = {
    'body': {
        'url': configuration['SCRAP_URL']
    }
}

mongo_helper.connect(configuration['DATABASE_URL'])