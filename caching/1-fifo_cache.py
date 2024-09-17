#!/usr/bin/python3
'''Module for FIFO caching'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''Caching system that follows FIFO algorithm'''
    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.keys_order = []
