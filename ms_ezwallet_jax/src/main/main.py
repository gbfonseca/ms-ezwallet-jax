from fastapi import FastAPI
from ms_ezwallet_jax.src.main.routes.actions import actions_router
from ms_ezwallet_jax.src.main.routes.get_actions import get_actions_router
from ms_ezwallet_jax.src.main.routes.healthcheck import healthcheck_router
import uvicorn
from ms_ezwallet_jax.src.main.config.configuration import configuration
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper

mongo_helper.connect(configuration['DATABASE_URL'])
app = FastAPI()

app.include_router(healthcheck_router)
app.include_router(actions_router)
app.include_router(get_actions_router)


def start():
    uvicorn.run("ms_ezwallet_jax.src.main.main:app",
                reload=True)


if __name__ == '__main__':
    start()
