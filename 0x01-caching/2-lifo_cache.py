#!/usr/bin/env python3
"""
lifo cache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        put: store to dict
        return none
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys()).pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.cache_data[key] = item

    def get(self, key):
        """
        retrive record
        """
        if key is not None:
            return self.cache_data.get(key)
