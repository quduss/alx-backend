#!/usr/bin/env python3
"""Server Class"""
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
        """paginate dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        my_tuple = index_range(page, page_size)

        my_list = []
        for i in range(my_tuple[0], my_tuple[1]):
            if i >= len(self.dataset()):
                return my_list
            my_list.append(self.__dataset[i])
        return my_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_hyper"""
        data = self.get_page(page, page_size)
        page_size_new = len(data)
        my_tuple = index_range(page, page_size)
        if my_tuple[1] >= len(self.dataset()):
            next_page = None
        else:
            next_page = page + 1
        prev_page = page - 1
        if prev_page == 0:
            prev_page = None
        total_pages = math.ceil(len(self.dataset()) / page_size)
        my_dict = {"page_size": page_size_new,
                   "page": page,
                   "data": data,
                   "next_page": next_page,
                   "prev_page": prev_page,
                   "total_pages": total_pages}
        return my_dict
