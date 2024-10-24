#!/usr/bin/env python3
'''Simple Pagination Module'''
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """Retrieve data from CSV file
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        data = []
        idx = index_range(page, page_size)
        if idx[0] < len(self.dataset()):
            for i in range(idx[0], idx[1]):
                data.append(self.dataset()[i])
        return data
