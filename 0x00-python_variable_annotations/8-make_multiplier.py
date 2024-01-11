#!/usr/bin/env python3
"""
a type annoted function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable"""
    def mul(fl: float):
        multiple: float = multiplier * multiplier
        return multiple
    return mul
