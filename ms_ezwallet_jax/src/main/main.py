from fastapi import FastAPI
from ms_ezwallet_jax.src.main.routes.actions import actions_router

app = FastAPI()

app.include_router(actions_router)
