#!/usr/bin/env python3
"""
script for a LRU caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LIFO cache system"""

    def __init__(self):
        super().__init__()
        self._items = OrderedDict()

    def put(self, key, item):
        """ put key value pair into cache"""
        if key and item:
            self._items[key] = item
            self.cache_data[key] = item
            self._items.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            popped_item = next(iter(self._items))
            del self.cache_data[popped_item]
            print("DISCARD:", popped_item)

        if len(self._items) > BaseCaching.MAX_ITEMS:
            self._items.popitem(last=False)

    def get(self, key):
        """ return item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
