#!/usr/bin/env python3
""" Authentication module for the API. """
from typing import List, TypeVar
from flask import request
import os


class Auth:
    """ Template class for authentication system. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if the path requires authentication. """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request. """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user from the request.
            For now, returns None.
        """
        return None

    def session_cookie(self, request=None):
        """ Retrieves the session cookie from the request.

        Args:
            request: The Flask request object.

        Returns:
            str: The session cookie value or None if not found.
        """

        if request is None:
            return None
        cookie = request.cookies.get(os.getenv('SESSION_NAME'))
        return cookie
