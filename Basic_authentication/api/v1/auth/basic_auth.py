#!/usr/bin/env python3
""" BasicAuth module for handling basic authentication """

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization
            header string.

        Returns:
            str: The Base64 encoded part of the header, or None if conditions
            aren't met.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self, auth_header_64: str) -> str:
        """Decodes the Base64 part of the Authorization header.
        """
        if auth_header_64 is None or type(auth_header_64) is not str:
            return None
        try:
            result = base64.b64decode(auth_header_64).decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            result = None
        return result

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Extracts user email and password from the decoded
        Base64 authorization header.

        Args:
            decoded_base64_authorization_header (str): The
            decoded Base64 string.

        Returns:
            (str, str): The user email and password as a tuple,
            or (None, None)
            if invalid.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email,
        password = decoded_base64_authorization_header.split(':', 1)
        return user_email, password
