from fastapi import APIRouter, Depends, HTTPException
from ms_ezwallet_jax.src.main.config.configuration import configuration


healthcheck_router = APIRouter(
    prefix="",
    tags=[""],
)


@healthcheck_router.get('/healthcheck')
async def perform_healthcheck():
    return {'healthcheck': 'Everything OK!'}
