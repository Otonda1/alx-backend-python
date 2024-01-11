#!/usr/bin/env python3
"""
return sum of a mixed
list as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the mixed list elements as a float."""
    return sum(mxd_lst)

