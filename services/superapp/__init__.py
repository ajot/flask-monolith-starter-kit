# services/superapp/__init__.py
# This file initializes the SuperApp service as a package and sets up the Blueprint for the SuperApp routes and templates.

from flask import Blueprint

# Create a Blueprint instance for the SuperApp service
superapp_bp = Blueprint('superapp', __name__, template_folder='templates')

# Import the routes for the SuperApp service
from . import superapp
