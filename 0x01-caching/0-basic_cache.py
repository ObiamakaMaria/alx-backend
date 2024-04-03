#!/usr/bin/python3
""" Implementing Caching Algorithm """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """The class for basic caching"""

    def put(self, key, item):
        """ Adding an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key:
            return self.cache_data.get(key)
        return None
