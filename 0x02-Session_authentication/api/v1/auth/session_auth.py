#!/usr/bin/env python3
"""
Module - session_auth
"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """class Session authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session id for user"""
        if user_id is None or not isinstance(user_id, str):
            return None
        sessionId = str(uuid.uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId
