#!/usr/bin/python3
'''LIFO Cache Module'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.last_key = None
