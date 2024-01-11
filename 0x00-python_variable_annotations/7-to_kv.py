#!/usr/bin/env python3
"""
a type-annoted function
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[Union[str, int]]:
    """returns a tuple"""
    tupleresult: Tuple[Union[int, float]] = (k, v*v)
    return tupleresult
