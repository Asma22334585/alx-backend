#!/usr/bin/python3
""" doc doc doc """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """doc doc doc"""

    def __init__(self):
        """doc doc doc"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """doc doc doc"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                least_frequency_keys = [
                    k for k, v in self.frequency.items() if v == min_frequency
                ]
                lfu_key = min(least_frequency_keys, key=self.frequency.get)
                self.cache_data.pop(lfu_key)
                self.frequency.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """doc doc doc"""
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data.get(key)
