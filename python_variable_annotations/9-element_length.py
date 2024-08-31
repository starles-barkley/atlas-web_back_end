#!/usr/bin/env python3
'''Defines a type-annotated function to
return lengths of iterable sequences.'''
from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    '''Return a list of tuples with each sequence and its length.'''
    return [(i, len(i)) for i in lst]\
