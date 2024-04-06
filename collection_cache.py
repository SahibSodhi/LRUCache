from collections import OrderedDict

class CollectionCache:
    def __init__(self):
        self.collections = {}

    def create_collection(self, collection_id, capacity):
        if collection_id in self.collections:
            raise ValueError("Collection already exists")
        self.collections[collection_id] = {'capacity': capacity, 'data': OrderedDict()}

    def update_capacity(self, collection_id, capacity):
        if collection_id not in self.collections:
            raise ValueError("Collection does not exist")
        self.collections[collection_id]['capacity'] = capacity

    def put_data(self, collection_id, key, value):
        if collection_id not in self.collections:
            raise ValueError("Collection does not exist")
        if len(self.collections[collection_id]['data']) >= self.collections[collection_id]['capacity']:
            self.evict_least_recently_used(collection_id)
        self.collections[collection_id]['data'][key] = value

    def evict_least_recently_used(self, collection_id):
        self.collections[collection_id]['data'].popitem(last=False)  # Pop the least recently used item

    def get_data(self, collection_id, key):
        if collection_id not in self.collections:
            raise ValueError("Collection does not exist")
        if key not in self.collections[collection_id]['data']:
            raise ValueError("Key not found")
        # Move the accessed item to the end to indicate it's most recently used
        value = self.collections[collection_id]['data'].pop(key)
        self.collections[collection_id]['data'][key] = value
        return value

    def get_collection_data(self, collection_id):
        if collection_id not in self.collections:
            raise ValueError("Collection does not exist")
        return self.collections[collection_id]['data']