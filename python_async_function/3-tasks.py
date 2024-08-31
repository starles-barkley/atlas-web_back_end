#!/usr/bin/env python3
'''
This script defines a regular function that creates and
returns an asyncio.Task for the `wait_random` coroutine,
which waits for a random delay between 0 and max_delay seconds.'''

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates and returns an asyncio.Task for
    the `wait_random` coroutine.'''
    return asyncio.create_task(wait_random(max_delay))
