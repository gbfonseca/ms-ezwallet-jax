from fastapi import APIRouter, Depends, HTTPException
from ..factories.get_action_data_by_code import make_get_action_data_by_code
from ..factories.get_actions import make_get_actions
from ms_ezwallet_jax.src.main.config.configuration import configuration


actions_router = APIRouter(
    prefix="/action",
    tags=["action"],
)


@actions_router.get('/{code}')
async def get_action_by_code(code: str):
    http_request = {
        'params': {
            'code': code
        }
    }
    get_action_data_by_code = make_get_action_data_by_code()
    response = get_action_data_by_code.handle(http_request)
    if(response['status_code'] != 200):
        raise HTTPException(
            status_code=response['status_code'], detail=response['body'])
    return response

