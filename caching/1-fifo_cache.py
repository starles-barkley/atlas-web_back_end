#!/usr/bin/python3
'''Module for FIFO caching'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''Caching system that follows FIFO algorithm'''
    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """Add an item to the cache using the FIFO algorithm"""
        if key is not None and item is not None:
            if key not in self.cache_data and len(
              self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.keys_order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            if key in self.cache_data:
                self.keys_order.remove(key)

            self.keys_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
