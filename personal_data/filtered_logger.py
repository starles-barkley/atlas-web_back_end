#!/usr/bin/env python3
'''This module contains a function for filtering log messages'''
import re

def filter_datum(fields, redaction, message, separator):
    '''Obfuscates fields in a log message'''
    pattern = f"({'|'.join(fields)})=([^\\{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
