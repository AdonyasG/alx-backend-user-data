#!/usr/bin/env python3
"""auth"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requre auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
