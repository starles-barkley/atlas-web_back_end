#!/usr/bin/env python3
'''This script defines an asynchronous routine `wait_n` that spawns the `wait_random`
coroutine multiple times and returns a list of delay times in ascending order.'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Asynchronous routine that spawns `wait_random` n times with the
    specified max_delay. Returns a list of all the delays in ascending order.'''

    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays