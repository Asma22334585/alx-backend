#!/usr/bin/env python3
""" MRU Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ class MRU """
    def __init__(self):
        """ inith method """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ item value for the key key """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.order.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.order.append(key)
        else:
            return None

    def get(self, key):
        """ self.cache_data linked to key """
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
