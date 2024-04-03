#!/usr/bin/env python3
"""
LIFO caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """ Add item into cache"""
        items_max = BaseCaching.MAX_ITEMS
        if key is not None or item is not None:
            self.cache_data[key] = item
        if key not in self._keys:
            self._keys.append(key)
        else:
            self._keys.append(self._keys.pop(self._keys.index(key)))
            if len(self._keys) > items_max:
                pop_key = self._keys.pop(-2)
                del self.cache_data[pop_key]
                print(f"DISCARD: {pop_key}")

    def get(self, key):
        """ return item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
