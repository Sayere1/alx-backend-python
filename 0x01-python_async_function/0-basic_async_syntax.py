#!/usr/bin/env python3
'''Asyn takes in an integer argument.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''max delay min 10 and wait time ranging from 0-10.'''
    time_spent = random.random() * max_delay
    await asyncio.sleep(time_spent)
    return time_spent
