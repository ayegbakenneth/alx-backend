#!/usr/bin/env python3
""" This is the file executable path """

def index_range(page, page_size):
    """ A function that returns a page and its size as a tuple """

    begining_index = (page - 1) * page_size
    end_index = begining_index + page_size - 1
    return begining_index, end_index
