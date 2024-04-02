#!/usr/bin/env python3
""" This helper function shows the starting and ending index"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculating the index range"""
    starting = (page - 1) * page_size
    ending = page * page_size
    return (starting, ending)
