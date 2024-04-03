#!/usr/bin/python3
""" LFU caching module """
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ The LFUCache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}  #To store the frequency of each key

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

            # Check if cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]

                least_recently_used_key = min(least_frequent_keys, key=lambda k: self.frequency.get(k, 0))

                if least_recently_used_key in self.cache_data:
                    del self.cache_data[least_recently_used_key]
                    del self.frequency[least_recently_used_key]
                    print("DISCARD:", least_recently_used_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
