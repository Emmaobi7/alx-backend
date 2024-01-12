#!/usr/bin/env python3
"""
lru module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    caching system
    """
    def __init__(self):
        """constructor"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        put: store value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                res = self.keys.pop(0)
                del self.cache_data[res]
                print(f"DISCARD: {res}")

    def get(self, key):
        """
        get: retrie data
        """
        if key is not None:
            return self.cache_data.get(key)
