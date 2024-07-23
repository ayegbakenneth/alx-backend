#!/usr/bin/env python3
""" The file executable path """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Create a class BasicCache that inherits from
    BaseCaching and is a caching system """

    def put(self, key, item):
        """ A method to add the key and value
        into the catch system """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
