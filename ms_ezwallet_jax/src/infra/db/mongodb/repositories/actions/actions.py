from ms_ezwallet_jax.src.data.protocols.add_actions_repository import AddActionsRepository
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper


class ActionsRepository(AddActionsRepository):

    def add(self, data: list):
        actions_collection = mongo_helper.get_collection('actions')
        actions = actions_collection.insert(data)
        return actions
