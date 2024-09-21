#!/usr/bin/env python3
""" Module for Session Authorization
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Session Authorization class that manages session-based authentication.

    Attributes:
        user_id_by_session_id (dict): Stores session IDs
        as keys and user IDs as values.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session ID for a user.

        Args:
            user_id (str): The ID of the user for whom the
            session is being created.

        Returns:
            str: The generated session ID, or None if the
            user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieve the User ID based on a given Session ID.

        Args:
            session_id (str): The session ID used to retrieve
            the associated user ID.

        Returns:
            str: The user ID if the session ID is valid, or None if invalid.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Return a User instance based on a cookie value """

        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)
