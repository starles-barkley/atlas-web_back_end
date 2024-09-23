#!/usr/bin/env python3
"""Flask App Module
"""

from flask import Flask, jsonify, abort, request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Return a welcome message in JSON format."""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """Register a new user.
    """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ Login Route for User
    """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        AUTH.create_session(email)
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
