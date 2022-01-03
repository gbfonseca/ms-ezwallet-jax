from fastapi import APIRouter, Depends, HTTPException
from ..factories.get_action_data_by_code import make_get_action_data_by_code

actions_router = APIRouter(
    prefix="/actions",
    tags=["actions"],
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
