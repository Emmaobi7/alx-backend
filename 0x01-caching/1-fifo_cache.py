#!/usr/bin/env python3
"""
FIFOIcache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOcaching: implemens sive constrict
    put
    get
    """
    def __init__(self):
        """
        constrctor
        """
        super().__init__()

    def put(self, key, item):
        """
        put: adds item to cache
        apply size constrict
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f'DISCARD: {first_key}')
            self.cache_data[key] = item

    def get(self, key):
        """
        get: get item from cache
        """
        if key is not None:
            return self.cache_data.get(key)
