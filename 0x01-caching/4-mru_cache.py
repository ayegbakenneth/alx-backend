#!/usr/bin/env python3
""" File executable path """

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching
""" Module importation path """


class MRUCache(BaseCaching):
    """  Class LRUCache that inherits from
    BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.most_used_item = OrderedDict()

    def put(self, key, item):
        """ A method for adding item into the cache """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.cache_data[key] = item
            self.most_used_item.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if len(self.most_used_item) > 0:
                    most_used = next(reversed(self.most_used_item))
                    del self.cache_data[most_used]
                    print("DISCARD: " + most_used)
            self.cache_data[key] = item
            self.most_used_item[key] = None

    def get(self, key):
        """ method to retrieve data from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.most_used_item.move_to_end(key)
        return self.cache_data[key]
