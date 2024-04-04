#!/usr/bin/env python3
"""Hypermedia pagination"""
import math
import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """"""
    current = page_size * page - page_size
    return (current, (page_size * page))

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
        """
        get a certain page
        """
        self.dataset()
        assert type(page_size) is int and type(page) is int
        assert page_size > 0
        assert page > 0
        x = index_range(page, page_size)
        if x[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[x[0]:x[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        
        """
        method returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer

        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        
        total_pages = math.ceil(total_items / page_size)

        return{
            "page": page,
            "page_size": page_size if page < total_pages else 0,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
            }
