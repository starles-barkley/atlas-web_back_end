#!/usr/bin/env python3
""" Module for Session Authorization
"""
from flask import request
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Authorization class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a session id for a user
        """

        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id
