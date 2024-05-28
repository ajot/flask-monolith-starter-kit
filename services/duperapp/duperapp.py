# services/duperapp/duperapp.py
# This file contains the logic and routes for the DuperApp service. 
# It defines the routes and their corresponding view functions.

from flask import render_template, jsonify
from . import duperapp_bp

# Define a route for the DuperApp service
@duperapp_bp.route('/')
def index():
    # Render the index.html template located in templates/duperapp/
    return render_template('duperapp/index.html')

# Define a route that takes an argument and returns it as JSON
@duperapp_bp.route('/echo/<message>')
def echo(message):
    # Return a JSON response with the provided message
    return jsonify({'message': message})
