#!/usr/bin/env python3
"""
Module - basic_auth
"""

import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64"""
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None

        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode base64 authorization header"""
        if base64_authorization_header is None or not isinstance(
                                             base64_authorization_header, str):
            return None
        try:
            base = base64.b64decode(base64_authorization_header)
            utf = base.decode('utf-8')
            return utf
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> tuple:
        """extract user credential"""
        if decoded_base64_authorization_header is None or not isinstance(
                            decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':')
        return email, password
