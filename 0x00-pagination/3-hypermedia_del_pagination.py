#!/usr/bin/env python3
""" Deletion-resilient hypermedia pagination """

import csv
import math
from typing import List, Dict
""" Importation file path """


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """defineing the class constructor"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ A method that return dictionary with key-value pairs """
        assert index is None or index >= 0
        dataset = self.dataset()
        begining_index = 0 if index is None else index
        end_index = begining_index + page_size
        end_index = min(end_index, len(dataset))
        page = dataset[begining_index:end_index]
        next_index = end_index if end_index < len(dataset) else None

        dict_result = {
            'index': begining_index,
            'next_index': next_index,
            'page_size': page_size,
            'data': page
        }

        return dict_result
