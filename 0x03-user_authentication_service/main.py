#!/usr/bin/env python3
"""
Module - main
"""

import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """register user"""
    user = {"email": email, "password": password}
    res = requests.post("http://0.0.0.0:5000/users", data=user)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}

    res = requests.post("http://0.0.0.0:5000/users",
                        data=user)
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """log in with wrong password"""
    user = {"email": email, "password": password}

    res = requests.post("http://0.0.0.0:5000/sessions", data=user)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """log in"""
    user = {"email": email, "password": password}

    res = requests.post("http://0.0.0.0:5000/sessions", data=user)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "logged in"}
    return res.cookies.get("session_id")


def profile_unlogged() -> None:
    """profile unlogged"""
    res = requests.get("http://0.0.0.0:5000/profile")
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """profile logged"""
    res = requests.get("http://0.0.0.0:5000/profile",
                       cookies={"session_id": session_id})
    assert res.status_code == 200
    assert res.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """log out"""
    res = requests.delete("http://0.0.0.0:5000/sessions",
                          cookies={"session_id": session_id})
    # assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """reset password token"""
    user = {"email": email}

    res = requests.post("http://0.0.0.0:5000/reset_password", data=user)
    assert res.status_code == 200
    assert "email" in res.json()
    assert res.json()["email"] == email
    assert type(res.json()["email"]) == str
    assert "reset_token" in res.json()
    assert type(res.json()["reset_token"]) == str
    return res.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """update password"""
    user = {"email": email, "reset_token": reset_token,
            "new_password": new_password}

    res = requests.put("http://0.0.0.0:5000/reset_password", data=user)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
