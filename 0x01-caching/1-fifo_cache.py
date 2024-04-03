#!/usr/bin/env python3
"""A script for FIFO caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""
    def __init__(self):
        ''' Initialising class instance. '''
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """ adds an item(key-value pair) into cache"""
        items_max = BaseCaching.MAX_ITEMS
        if key is not None or item is not None:
            self.cache_data[key] = item
            self._keys.append(key)
            if key not in self._keys:
                self._keys.append(key)
            if len(self._keys) >= items_max:
                # popping first item in list i.e. FIFO
                pop_key = self._keys.pop(0)
                del self.cache_data[pop_key]
                print(f"DISCARD: {pop_key}")

    def get(self, key):
        """
        retrieves the value in cache associated with key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
