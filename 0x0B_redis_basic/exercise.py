#!/bin/user/env python3
import redis
import uuid
from typing import Union, Callable, Optional
import functools

def count_calls(method: Callable) -> Callable:
    """A decorator that increments a counter in Redis every time the method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the input arguments and outputs of a function in Redis lists.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output

    return wrapper

class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        """Retrieve a string from Redis by key, converting the byte data to a UTF-8 string."""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis by key, converting the byte data to an integer."""
        return self.get(key, lambda d: int(d))

    def get_call_history(self, method_name: str):
        """Retrieve the call history of a method's inputs and outputs from Redis."""
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"
        
        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        return {"inputs": inputs, "outputs": outputs}
        
    def replay(method: Callable) -> None:
        """
        Display the history of calls of a particular function, showing inputs and outputs.
        """
        self = method.__self__
        method_name = method.__qualname__

        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        call_count = len(inputs)

        print(f"{method_name} was called {call_count} times:")

        for input_args, output in zip(inputs, outputs):
            print(f"{method_name}(*{input_args.decode('utf-8')}) -> {output.decode('utf-8')}")
