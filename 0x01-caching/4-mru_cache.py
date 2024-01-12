#!/usr/bin/env python3
"""
MRU Caching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    caching system
    """
    def __init__(self):
        """constructor"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        put: remove most recent used value
        using mru algorithm
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = self.order.pop(-2)
            del self.cache_data[mru]
            print(f"DISCARD: {mru}")

    def get(self, key):
        """
        get: retieve record
        """
        if key is not None:
            return self.cache_data.get(key)
