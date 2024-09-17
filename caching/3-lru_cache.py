#!/usr/bin/python3
'''LRU Cache Module'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
  '''Caching system that follows the LRU alogrithm'''
    def __init__(self):
        '''Initialize the LRU cache'''
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        '''Add an item to the cache using the LRU algorithm'''
        if key is not None and item is not None:
            if key not in self.cache_data and len(
              self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            
            if key in self.cache_data:
                self.access_order.remove(key)
            
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        '''Retrieve an item from the cache'''
        if key is None or key not in self.cache_data:
            return None
        
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]