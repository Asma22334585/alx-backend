#!/usr/bin/python3
""" Basic dictionary """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ caching system"""

    def put(self, key, item):
        """assign to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """value in self.cache_data linked to key"""
        return self.cache_data.get(key)
