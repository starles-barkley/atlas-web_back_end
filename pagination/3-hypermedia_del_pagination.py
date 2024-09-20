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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''Retrieve info with pagination details'''
        if page < 1 or page_size < 1:
            return {
                'page': page,
                'page_size': page_size,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': 0
            }

        dataset = self.dataset()
        total_data = len(dataset)
        total_pages = math.ceil(total_data / page_size)
        start, end = index_range(page, page_size)

        data = dataset[start:end]

        return {
            'page': page,
            'page_size': page_size,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Retrieve data from the dataset based on the starting index and page size.'''
        if index is None:
            index = 0
        assert index >= 0, "Index must be a non-negative integer."
        assert page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        total_data = len(dataset)
        
        start_index = index
        end_index = index + page_size

        if start_index >= total_data:
            return {
                'index': start_index,
                'next_index': None,
                'page_size': page_size,
                'data': []
            }

        data = dataset[start_index:end_index]

        return {
            'index': start_index,
            'next_index': end_index if end_index < total_data else None,
            'page_size': page_size,
            'data': data
        }
