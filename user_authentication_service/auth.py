#!/usr/bin/env python3
"""auth module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with an email and password.
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials by checking the
        provided email and password.
        """
        try:
            user = self._db.find_user_by(email=email)
            checked_pw = password.encode('utf-8')
            hashed_pw = user.hashed_password
            return bcrypt.checkpw(checked_pw, hashed_pw)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Create a new session ID
        """

        try:
            user = self._db.find_user_by(email=email)
            new_session = _generate_uuid()
            self._db.update_user(user.id, session_id=new_session)
            return new_session
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt.
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generate a new UUID
    """

    return str(uuid.uuid4())
