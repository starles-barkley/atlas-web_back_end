#!/usr/bin/env python3
'''This script defines an asynchronous coroutine
that waits for a random delay between 0 and a
specified maximum value and returns
the actual delay time as a float.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and returns the actual delay'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
