from ms_ezwallet_jax.src.presentation.controllers.actions.get_action_data_by_code import GetActionDataByCodeController
from ms_ezwallet_jax.src.infra.http_client.requests import RequestsAdapter


def make_get_action_data_by_code() -> GetActionDataByCodeController:
    requests_adapter = RequestsAdapter()
    get_action_data_by_code = GetActionDataByCodeController(requests_adapter)
    return get_action_data_by_code
