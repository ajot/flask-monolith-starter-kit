# services/duperapp/__init__.py
# This file initializes the DuperApp service as a package and sets up the Blueprint 
# for the DuperApp routes and templates.

from flask import Blueprint

# Create a Blueprint instance for the DuperApp service
duperapp_bp = Blueprint('duperapp', __name__, template_folder='templates')

# Import the routes for the DuperApp service
from . import duperapp
