#!/usr/bin/env python3
'''Defines a type-annotated function to
return lengths of iterable sequences.'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return a list of tuples with each sequence and its length.'''
    return [(i, len(i)) for i in lst]
