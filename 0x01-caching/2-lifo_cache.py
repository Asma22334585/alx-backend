#!/usr/bin/python3
""" LIFO caching """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO"""

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """tem value for the key key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = list(self.cache_data.keys())[-1]
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item

    def get(self, key):
        """value in self.cache_data linked to key"""
        return self.cache_data.get(key)
