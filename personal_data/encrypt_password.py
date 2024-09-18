#!/usr/bin/env python3
'''This module contains functions for password hashing.'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Hashes a password using bcrypt with automatic salting.'''
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
