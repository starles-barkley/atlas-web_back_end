#!/usr/bin/env python3
'''Defines a type-annotated function that returns a multiplier function.'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return a function that multiplies a float by the given multiplier.'''
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
