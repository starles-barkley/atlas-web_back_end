#!/usr/bin/python3
'''Basic_cache script'''

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key)
