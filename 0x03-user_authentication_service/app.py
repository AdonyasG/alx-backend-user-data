#!/usr/bin/env python3
"""Module app"""

from flask import Flask, jsonify, request, abort, redirect, make_response
from auth import Auth

app = Flask(__name__)
Auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """index"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """endpoint to register users"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login endpoint"""
    email = request.form.get('email')
    password = request.form.get('password')
    responses = {"email": email, "message": "logged in"}
    if Auth.valid_login(email, password):
        session_id = Auth.create_session(email)
        response = make_response(jsonify(responses))
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
