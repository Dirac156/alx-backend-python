#!/usr/bin/env python3
"""module to perform some actions"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """return tuple"""
    return (k, pow(v, 2))
