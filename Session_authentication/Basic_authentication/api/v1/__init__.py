#!/usr/bin/env python3
""" Views package initializer """

from flask import Blueprint

# Initialize Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views (routes) that use the app_views Blueprint
from api.v1.views.index import *
