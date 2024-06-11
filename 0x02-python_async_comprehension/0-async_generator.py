#!/usr/bin/env python3
'''Write a coroutine called async_generator that takes no arguments.'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''coroutine will loop 10x each time asyn wait 1 sec then sample 0-10.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
