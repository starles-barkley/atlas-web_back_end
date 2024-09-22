#!/usr/bin/env python3
"""Auth Module"""

import bcrypt

def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt.
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
