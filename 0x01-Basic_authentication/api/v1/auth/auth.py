#!/usr/bin/env python3
"""
Module - auth
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requre auth"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        for exclude_path in excluded_paths:
            if exclude_path.endswith('/'):
                if path.startswith(exclude_path.rstrip('/')):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
