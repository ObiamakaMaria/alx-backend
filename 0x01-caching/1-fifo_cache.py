#!/usr/bin/python3
"""Fifo caching algorithm Module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """The class for FIFO caching"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                self.cache_data[key] = item
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key:
            return self.cache_data.get(key)
        return None
