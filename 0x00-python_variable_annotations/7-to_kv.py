#!/usr/bin/env python3
'''type-annotated func to_kv that takes a string k, int OR float v as arg'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''when compute they return a tuple.'''
    return (k, float(v**2))
