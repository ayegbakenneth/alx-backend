#!/usr/bin/env python3
""" File executable path """

BaseCaching = __import__('base_caching').BaseCaching
""" File import path """


class LIFOCache(BaseCaching):
    """ A class that inherits from BaseCaching
    and is a caching system """
    def __init__(self):
        """ The constructor method """
        super().__init__()
        self.track_list = []

    def put(self, key, item):
        """ Method that add items to the cache """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = self.track_list.pop()
                del self.cache_data[last_item]
                print(f"DISCARD: {last_item}\n")
        self.cache_data[key] = item
        self.track_list.append(key)

    def get(self, key):
        """ A method that returns the cache data """
        return self.cache_data[key]
        if key is None or key not in self.cache_data:
            return None
