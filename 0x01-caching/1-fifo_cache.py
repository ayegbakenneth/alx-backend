#!/usr/bin/env python3
""" File execution path """

BaseCaching = __import__('base_caching').BaseCaching
""" Module import path """


class FIFOCache(BaseCaching):
    """ class FIFOCache that inherits from
    BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Method to add data to the cache """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print("DISCARD:" + " " + first_item)
        self.cache_data[key] = item

    def get(self, key):
        """ A method that return the cache data """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
