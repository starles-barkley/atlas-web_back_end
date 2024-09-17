#!/usr/bin/python3
'''LIFO Cache Module'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        if key is not None and item is not None:
            if key not in self.cache_data and len(
              self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key)
