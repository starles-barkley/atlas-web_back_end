#!/usr/bin/python3
'''Basic_cache script'''

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
  '''Defines a caching system with no item limit & 
  inherits from BaseCaching.'''
  def put(self, key, item):
    """Assigns the item to the cache_data dictionary using the key."""
    if key is not None and item is not None:
      self.cache_data[key] = item

  def get(self, key):
    """Returns the value linked to the key in cache_data."""
    if key is None:
        return None
      return self.cache_data.get(key)
