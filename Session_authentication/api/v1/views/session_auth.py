#!/usr/bin/env python3
""" Module for Session Authentication routes
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User

@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=False)
def login():
    """ Handles the login for session authentication """
    
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search(email=email)
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    session_name = getenv("SESSION_NAME", "_my_session_id")
    response.set_cookie(session_name, session_id)

    return response
