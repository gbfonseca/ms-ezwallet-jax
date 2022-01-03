from ms_ezwallet_jax.src.data.protocols.add_actions_repository import AddActionsRepository
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper


class ActionsRepository(AddActionsRepository):

    def add(self, data: list):
        actions_collection = mongo_helper.get_collection('actions')
        saved_actions = []
        for action in data:
            act = actions_collection.find_one_and_update(
                {'code': action['code']}, {'$set': action}, upsert=True)
            saved_actions.append({
                'id': str(act['_id']),
                'code': act['code']
            })

        return saved_actions
