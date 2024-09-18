#!/usr/bin/env python3
""" Authentication module for the API. """
from typing import List, TypeVar
from flask import request


class Auth:
    """ Template class for authentication system. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if the path requires authentication.
            For now, returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request.
            For now, returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user from the request.
            For now, returns None.
        """
        return None
