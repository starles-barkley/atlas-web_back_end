#!/usr/bin/python3
'''LRU Cache Module'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
  '''Caching system that follows the LRU alogrithm'''
    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.access_order = []
