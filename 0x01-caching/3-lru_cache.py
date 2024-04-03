#!/usr/bin/env python3
"""
script for a LRU caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """ put key value pair into cache"""
        items_max = BaseCaching.MAX_ITEMS
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self._keys:
                self._keys.append(key)
            else:
                self._keys.append(self._keys.pop(self._keys.index(key)))
        if len(self._keys) > items_max:
            popped_key = self._keys.pop(0)
            del self.cache_data[popped_key]
            print(f"DISCARD: {popped_key}")

    def get(self, key):
        """ get item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
