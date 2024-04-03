 #!/usr/bin/env python3
"""
script for a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching
    """

    def put(self, key, item):
        """
        adds an item into cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ 
        retrieves the value in cache associated with key
        Args:
            key
        """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
