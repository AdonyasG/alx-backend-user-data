#!/usr/bin/env python3
"""
Module - basic_auth
"""

import base64
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """fetch credential from user object"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        listt = User.search({'email': user_email})
        if not listt:
            return None
        user = listt[0]
        if user.is_valid_password(user_pwd):
            return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get curren user from the req"""
        header = self.authorization_header(request)
        b64_token = self.extract_base64_authorization_header(header)
        token = self.decode_base64_authorization_header(b64_token)
        email, pwd = self.extract_user_credentials(token)
        user = self.user_object_from_credentials(email, pwd)
        return user
