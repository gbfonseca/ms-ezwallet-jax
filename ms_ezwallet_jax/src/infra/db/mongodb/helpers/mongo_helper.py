from pymongo import MongoClient, collection
import json
from bson import json_util, ObjectId


class MongoHelper():
    client: MongoClient

    def connect(self, config: str):
        self.client = MongoClient(config)

    def disconnect(self):
        self.client.close()
        self.client = None

    def get_collection(self, name: str) -> collection.Collection:
        return self.client.get_database('jax').get_collection(name)
    
    def parse(data):
        print(data)
        return json.loads(json_util.dumps(data))


mongo_helper = MongoHelper()
