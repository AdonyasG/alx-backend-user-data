#!/usr/bin/env python3
"""
Module - session_auth
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """class Session authentication"""
    user_id_by_session_id = {}
