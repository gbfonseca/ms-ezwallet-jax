from fastapi import APIRouter, Depends, HTTPException
from ..factories.get_action_data_by_code import make_get_action_data_by_code
from ..factories.get_actions import make_get_actions
from ms_ezwallet_jax.src.main.config.configuration import configuration


get_actions_router = APIRouter(
    prefix="/actions",
    tags=["actions"],
)

@get_actions_router.get('')
async def get_actions():
    http_request = {
        'body': {
            'url': configuration['SCRAP_URL']
        }
    }

    get_actions = make_get_actions()
    response = get_actions.handle(http_request)
    
    if(response['status_code'] != 200):
        raise HTTPException(
            status_code=response['status_code'], detail=response['body'])
    return response