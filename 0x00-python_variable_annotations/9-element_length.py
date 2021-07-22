#!/usr/bin/env python3
"""module element length"""
from typing import List, Sequence, Tuple


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """iterate through sequence"""
    return [(i, len(i)) for i in lst]
