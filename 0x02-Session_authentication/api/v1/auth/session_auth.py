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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns userId based on sessionId"""
        if session_id is None or not isinstance(session_id, str):
            return None
        userId = self.user_id_by_session_id.get(session_id)
        return userId
