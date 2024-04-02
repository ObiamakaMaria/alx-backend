#!/usr/bin/env python3
"""
This implements Deletion-resilient hypermedia pagination
"""

import math
import csv
from typing import List, Dict


class Server:
    """The server class paginates a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as b:
                reader = csv.reader(b)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        This function ensures that the user gets the correct 
        page of data even if some rows have been removed 
        from the dataset between queries
        """
        assert isinstance(index, int) and isinstance(page_size, int)
        assert index >= 0 and page_size > 0
        indexed_dataset = self.indexed_dataset()
        assert index < len(indexed_dataset)
        data = []
        next_index = index
        for _ in range(page_size):
            while not indexed_dataset.get(next_index):
                next_index += 1
            data.append(indexed_dataset[next_index])
            next_index += 1
        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
