from ms_ezwallet_jax.src.data.protocols.add_actions_repository import AddActionsRepository
from ms_ezwallet_jax.src.infra.db.mongodb.helpers.mongo_helper import mongo_helper
from pymongo import UpdateOne
import uuid


class ActionsRepository(AddActionsRepository):

    def add(self, data: list):
        actions_collection = mongo_helper.get_collection('actions')
        saved_actions = []
        requests = []
        for action in data:
            action['_id'] = str(uuid.uuid4())
            requests.append(UpdateOne({'code': action['code']}, {
                '$set':  {'code': action['code']}}, upsert=True))
        actions_collection.bulk_write(requests)
        actions = actions_collection.find()
        for document in actions:
            saved_actions.append({
                'id': str(document['_id']),
                'code': document['code']
            })
        return saved_actions
