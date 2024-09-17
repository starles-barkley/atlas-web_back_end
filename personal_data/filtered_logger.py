#!/usr/bin/env python3
'''This module contains a function for filtering log messages'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    '''Obfuscates fields in a log message'''
    pattern: str = f"({'|'.join(fields)})=([^\\{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
