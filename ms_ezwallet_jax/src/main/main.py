from fastapi import FastAPI
from ms_ezwallet_jax.src.main.routes.actions import actions_router
import uvicorn

app = FastAPI()

app.include_router(actions_router)


def start():
    uvicorn.run("ms_ezwallet_jax.src.main.main:app",
                host="0.0.0.0", port=8000, reload=True)


if __name__ == '__main__':
    start()
