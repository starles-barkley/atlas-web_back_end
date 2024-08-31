#!/usr/bin/env python3
'''This script defines function task_wait_n that runs multiple
tasks using task_wait_random and returns a sorted list of delays. '''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Runs task_wait_random n times with a maximum delay of max_delay
    and returns the delays in ascending order.'''

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
