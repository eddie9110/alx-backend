#!/usr/bin/python3
"""script for a MRU caching system"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU Caching"""
    def __init__(self):
        super().__init__()
        self._items = OrderedDict()

    def put(self, key, item):
        """ put key value pair into cache"""
        if key and item:
            self.cache_data[key] = item
            self._items[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped_key = next(iter(self._items))
                del self.cache_data[popped_key]
                print("DISCARD:", popped_key)
            if len(self._items) > BaseCaching.MAX_ITEMS:
                self._items.popitem(last=False)
            self._items.move_to_end(key, False)

    def get(self, key):
        """ return item by key"""
        if key in self.cache_data:
            self._items.move_to_end(key, False)
            return self.cache_data[key]
        return None
