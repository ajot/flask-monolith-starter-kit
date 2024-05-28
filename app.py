# app.py
# This is the main application script where the Flask app is defined and run. 
# It initializes the app, configures it, registers Blueprints for each service, and defines the home route.

import os
from dotenv import load_dotenv
from flask import Flask, render_template
from services.superapp import superapp_bp
from services.duperapp import duperapp_bp

# Load environment variables from a .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configure the secret key for session management and security (recommended practice)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

    # Register Blueprints for the SuperApp and DuperApp services
    app.register_blueprint(superapp_bp, url_prefix='/superapp')
    app.register_blueprint(duperapp_bp, url_prefix='/duperapp')

    # Define the home route
    @app.route('/')
    def home():
        # Render the home page template
        return render_template('home.html')

    return app

if __name__ == '__main__':
    # Create the app instance
    app = create_app()
    
    # Run the Flask application in debug mode
    app.run(debug=True)
