#!/usr/bin/env python3
'''Defines a type-annotated function to
return a tuple from a string and an int/float.'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return a tuple with a string and the square of an int/float.'''
    return (k, float(v ** 2))
