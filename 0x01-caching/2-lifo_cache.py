#!/usr/bin/python3
""" Lifo caching algorithm Module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """The class for LIFO caching"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item) -> None:
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                first_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """  Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None
