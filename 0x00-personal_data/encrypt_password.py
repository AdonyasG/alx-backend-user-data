#!/usr/bin/env python3
"""encrypt_password"""

import bcrypt


def hash_password(password):
    """simple password hashing"""
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pw
