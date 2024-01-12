#!/usr/bin/env python3
"""
lfu caching algorithm module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    caching system
    """
    def __init__(self):
        """constructor"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """
        put: store value
        lfu algorith,
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] = 1
        else:
            self.cache_data[key] = item
            self.freq[key] += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_keys = [k for k, v in self.freq.items() if v == min(self.freq.values())]

        if len(lfu_keys) > 1:
            lru_key = min(self.cache_data, key=lambda k: self.access_order[k])
            lfu_keys = [lfu]

        discard_key = lfu_keys[0]
        del self.cache_data[discard_key]
        del self.freq[discard_key]
        print(f"DISCARD: {discard_key}")


    def get(self, key):
        """
        get: retieve record
        """
        if key is not None:
            return self.cache_data.get(key)
