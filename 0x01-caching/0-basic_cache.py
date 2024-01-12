#!/usr/bin/env python3
"""
basiccache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    define basic caching methods
    get
    put
    """

    def put(self, key, item):
        """
        put: add item to cache
        Args:
            key: hash table key
            item: value
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get: get item by kyey
        Args:
            key: key to data
        """
        if key is not None:
            return self.cache_data.get(key)
