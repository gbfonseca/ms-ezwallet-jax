from ms_ezwallet_jax.src.domain.usecases.add_actions import AddActions
from ms_ezwallet_jax.src.data.protocols.add_actions_repository import AddActionsRepository


class DbAddActionsAdapter(AddActions):
    def __init__(self, add_actions_repository: AddActionsRepository):
        self.add_actions_repository = add_actions_repository

    def add(self, data: list):
        actions = self.add_actions_repository.add(data)
        return actions
