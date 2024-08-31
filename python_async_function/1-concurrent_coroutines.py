#!/usr/bin/env python3
'''This script defines an asynchronous routine `wait_n` that spawns the `wait_random`
coroutine multiple times and returns a list of delay times in ascending order.'''

import asyncio
from typing import List
from previous_script import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronous routine that spawns `wait_random` n times
    with the specified max_delay. Returns a list of all the delays
    in ascending order."""

    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    
    return delays