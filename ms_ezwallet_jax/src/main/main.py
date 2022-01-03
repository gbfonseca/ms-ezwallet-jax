from fastapi import FastAPI
from ms_ezwallet_jax.src.main.routes.actions import actions_router
import uvicorn
from ms_ezwallet_jax.src.main.config.configuration import configuration
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper
from ms_ezwallet_jax.src.main.factories.get_actions import makeGetActions

app = FastAPI()

app.include_router(actions_router)


def start():
    
    get_actions = makeGetActions()
    http_request = {
        'body': {
            'url': configuration['SCRAP_URL']
        }
    }
    mongo_helper.connect(configuration['DATABASE_URL'])
    get_actions.handle(http_request)
    uvicorn.run("ms_ezwallet_jax.src.main.main:app",
                host="0.0.0.0", port=8000, reload=True)

if __name__ == '__main__':
    start()




