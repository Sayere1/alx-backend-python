#!/usr/bin/env python3
'''write a coroutine called async_comprehension by importing asyn_generator'''
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Using an async comprehensing over async_generator.'''
    return [rn async for rn in async_generator()]
