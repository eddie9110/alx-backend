#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """ function returns a Tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters."""
    current = page_size * page - page_size
    return (current, (page_size * page))
