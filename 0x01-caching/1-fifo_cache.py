#!/usr/bin/python3
""" FIFO caching """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """doc doc doc"""

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """tem value for the key key"""
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = next(iter(self.cache_data))
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item

    def get(self, key):
        """value in self.cache_data linked to key"""
        return self.cache_data.get(key)
