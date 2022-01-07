from ms_ezwallet_jax.src.data.protocols.add_actions_repository import AddActionsRepository
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper
from pymongo import UpdateOne


class ActionsRepository(AddActionsRepository):

    def add(self, data: list):
        actions_collection = mongo_helper.get_collection('actions')
        saved_actions = []
        requests = []
        for action in data:
            requests.append(UpdateOne({'code': action['code'], 'type': action['type']}, {
                '$set':  action}, upsert=True))
        actions_collection.bulk_write(requests)
        actions = actions_collection.find()
        for document in actions:
            saved_actions.append({
                'id': str(document['_id']),
                'code': document['code'],
                'type': document['type']
            })
        return saved_actions
