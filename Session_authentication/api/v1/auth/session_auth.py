#!/usr/bin/env python3
""" Module for Session Authentication """

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ SessionAuth class that manages session authentication """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a given user_id.

        Args:
            user_id (str): The ID of the user for whom the
            session ID is being created.

        Returns:
            str: The session ID, or None if user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id =
