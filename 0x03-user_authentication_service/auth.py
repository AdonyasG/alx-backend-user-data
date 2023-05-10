#!/usr/bin/env python3
"""encrypt_password"""
from typing import ByteString
import bcrypt
from db import DB, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """simple password hashing"""
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pw


def _generate_uuid() -> str:
    """generates str representation of UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initialization"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user"""
        try:
            if type(self._db.find_user_by(email=email) is User):
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            password = _hash_password(password)
            user = self._db.add_user(email, password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """valid login"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """create a session"""
        try:
            user = self._db.find_user_by(email=email)
            sessionId = _generate_uuid()
            userId=user.id
            self._db.update_user(userId, session_id=sessionId)
            return sessionId
        except Exception:
            return None
