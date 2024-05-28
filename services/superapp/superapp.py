# services/superapp/superapp.py
# This file contains the logic and routes for the SuperApp service. 
# It defines the routes and their corresponding view functions.

from flask import render_template, jsonify
from . import superapp_bp

# Define a route for the SuperApp service
@superapp_bp.route('/')
def index():
    # Render the index.html template located in templates/superapp/
    return render_template('superapp/index.html')

# Define a route that takes an argument and returns it as JSON
@superapp_bp.route('/echo/<message>')
def echo(message):
    # Return a JSON response with the provided message
    return jsonify({'message': message})
