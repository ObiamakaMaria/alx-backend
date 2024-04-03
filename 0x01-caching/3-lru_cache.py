#!/usr/bin/python3
""" LRU caching algorithm Module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """The class for LRU caching"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item) -> None:
        """Add an item in the cache """
        if key and item:
            if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data.keys():
            item = self.cache_data.get(key)
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
