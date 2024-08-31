#!/usr/bin/env python3
''' This script defines an asynchronous function `measure_runtime` that measures
the total execution time for running the `async_comprehension` coroutine
four times concurrently.'''

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing the `async_comprehension` coroutine
    four times concurrently.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    total_time = time.perf_counter() - start_time
    return total_time
