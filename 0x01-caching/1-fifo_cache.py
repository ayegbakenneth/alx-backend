#!/usr/bin/env python3
""" File execution path """

from collections import deque
BaseCaching = __import__('base_caching').BaseCaching
""" Module import path """


class FIFOCache(BaseCaching):
    """ class FIFOCache that inherits from
    BaseCaching and is a caching system """
    def __init__(self):
        """ The class constructor """
        super().__init__()
        self.item_tracker = deque()

    def put(self, key, item):
        """ Method to add data to the cache """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = self.item_tracker.popleft()
                del self.cache_data[first_item]
                print("DISCARD:" + " " + first_item)
        self.cache_data[key] = item
        self.item_tracker.append(key)

    def get(self, key):
        """ A method that return the cache data """
        if key is None or key not in self.cache_data:
            return self.cache_data[key]
        return None
