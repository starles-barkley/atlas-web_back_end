#!/usr/bin/env python3
""" Module of Index views """

from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return: the status of the API
    """
    return jsonify({"status": "OK"})

@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized():
    """ Unauthorized error """
    abort(401)

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden_endpoint():
    """ Endpoint to trigger 403 error """
    abort(403)
