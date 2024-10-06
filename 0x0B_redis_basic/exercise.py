#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional
import functools

def count_calls(method: Callable) -> Callable:
    """
    A decorator that increments a counter in Redis every time the method is called.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wraps the original method and increments the call count in Redis."""
        key = method.__qualname__
        
        self._redis.incr(key)
        
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieve data from Redis by key, optionally converting it using a provided callable.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis by key, converting the byte data to a UTF-8 string.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis by key, converting the byte data to an integer.
        """
        return self.get(key, lambda d: int(d))
