#!/usr/bin/python3
""" LRU Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """class LRU"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """item value for the key key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.order.pop(0)
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """self.cache_data linked to key"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
