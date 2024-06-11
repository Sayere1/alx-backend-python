#!/usr/bin/env python3
'''Import async_comprehension and write a measure_runtime'''
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''coroutine will exe async_comprehension 4X in parallel using asyncio.'''
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.time() - start_time
