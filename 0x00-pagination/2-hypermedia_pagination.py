#!/usr/bin/env python3
""" File executable path """

from typing import List
import csv
import math
""" File importation path """


def index_range(page, page_size):
    """ File executable path """

    begining_index = (page - 1) * page_size
    end_index = begining_index + page_size - 1
    return begining_index, end_index

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method to validate the input data"""
        assert isinstance(page, int) and page > o
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        begining_index, end_index = index_range(page, page_size)

        if begining_index >= len(dataset):
            return []
        begining_index, end_index = self.index_range(page, page_size)
        return dataset[begining_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        page_with_dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_dict = {
            "page_size": len(page_with_dataset),
            "page": page,
            "data": page_with_dataset,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_dict
