# Flask Monolith Example

This repository provides a starter kit for using Flask to build a monolithic application. It uses Flask Blueprints to modularize services, making the codebase more organized and maintainable. The benefits of using Blueprints include simplified development, easier maintenance, and better scalability.

This starter kit includes two fictitious services: SuperApp and DuperApp. You can replace these services with your own or add more services to build additional functionalities. This serves as a sample to help you get started with building a modular Flask application.

## Directory Structure

The application is structured as follows:

```
/flask-monolith-example
|____app.py # Main application script where the Flask app is defined and run.
|____requirements.txt # Lists all project dependencies for pip installation.
|____static # Directory for static files like CSS, JS, and images.
| |____images
| | |____logo.png # Placeholder for a logo image.
|____templates # Jinja2 templates directory.
| |____home.html # Template for the home page.
| |____base.html # Base template that other templates extend.
| |____superapp # Templates specific to the SuperApp service.
| | |____index.html
| |____duperapp # Templates specific to the DuperApp service.
| | |____index.html
|____services # Python code for services.
| |____superapp
| | |____init.py # Initializes superapp as a package.
| | |____superapp.py # Contains logic and routes for superapp.
| |____duperapp
| | |____init.py # Initializes duperapp as a package.
| | |duperapp.py # Contains logic and routes for duperapp.
|.env.example # Example environment variables configuration.
```

## Setting Up the Application

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ajot/flask-monolith-example.git
    cd flask-monolith-example
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    Rename the `.env.example` file to `.env`:

    ```sh
    mv .env.example .env
    ```

    Edit the `.env` file to include your own secret key:

    ```env
    SECRET_KEY=your-very-secret-key
    ```

    **Important Note:** Do not commit the `.env` file to version control. Add `.env` to your `.gitignore` file to prevent sensitive information from being exposed.

### Running the Application

1. **Run the application:**

    ```sh
    python app.py
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000/`.

## Application Structure and Blueprints

This application uses Flask Blueprints to organize the code into separate modules. Each service (SuperApp and DuperApp) has its own directory, containing the necessary files to define the routes and logic for that service.

### SuperApp Service

- **Route:** `/superapp`
- **Directory:** `services/superapp`
- **Blueprint Initialization:**
    - `services/superapp/__init__.py`
    - `services/superapp/superapp.py`
- **Template Location:** `templates/superapp`

### DuperApp Service

- **Route:** `/duperapp`
- **Directory:** `services/duperapp`
- **Blueprint Initialization:**
    - `services/duperapp/__init__.py`
    - `services/duperapp/duperapp.py`
- **Template Location:** `templates/duperapp`

## Adding a New Service

To add a new service to this application, follow these steps:

1. **Create Service Directory**:
   - Navigate to the `services/` directory.
   - Create a new directory for your service, e.g., `newservice`.

2. **Initialize Service**:
   - Inside the `newservice` directory, create an `__init__.py` file. This file should initialize a Flask Blueprint.
   - Create a `newservice.py` file where you will define the routes and logic of your new service.

3. **Define Blueprint in `newservice.py`**:
   ```python
   from flask import Blueprint, render_template

   newservice_bp = Blueprint('newservice', __name__, template_folder='templates')

   @newservice_bp.route('/')
   def index():
       return render_template('newservice/index.html')
   ```

4. **Create Templates**:
   - Navigate to `templates/`.
   - Create a directory named `newservice`.
   - Add `index.html`, `base.html`, and any other templates needed.

5. **Register Blueprint**:
   - Open `app.py`.
   - Import and register the Blueprint:
     ```python
     from flask import Flask, render_template
     from services.newservice import newservice_bp

     def create_app():
         app = Flask(__name__)
         app.config['SECRET_KEY'] = 'your-secret-key'

         # Register Blueprints
         app.register_blueprint(newservice_bp, url_prefix='/newservice')
         app.register_blueprint(superapp_bp, url_prefix='/superapp')
         app.register_blueprint(duperapp_bp, url_prefix='/duperapp')

         @app.route('/')
         def home():
             return render_template('home.html')

         return app

     if __name__ == '__main__':
         app = create_app()
         app.run(debug=True)
     ```

6. **Run and Test**:
   - Ensure everything is working as expected by starting your Flask application and navigating to the routes defined in your new service.

## Adding a New Endpoint

To add a new endpoint to an existing service, follow these steps:

1. **Define the New Route**:
   - Open the service file, e.g., `superapp.py` or `duperapp.py`.
   - Add a new route that accepts an argument and returns it as JSON.

   **Example for SuperApp**:

   ```python
   from flask import render_template, jsonify
   from . import superapp_bp

   @superapp_bp.route('/')
   def index():
       return render_template('superapp/index.html')

   @superapp_bp.route('/echo/<message>')
   def echo(message):
       return jsonify({'message': message})
   ```

   **Example for DuperApp**:

   ```python
   from flask import render_template, jsonify
   from . import duperapp_bp

   @duperapp_bp.route('/')
   def index():
       return render_template('duperapp/index.html')

   @duperapp_bp.route('/echo/<message>')
   def echo(message):
       return jsonify({'message': message})
   ```

2. **Update Home Page Links**:
   - Open `templates/home.html`.
   - Add links to the new endpoints.

   ```html
   {% extends "base.html" %}

   {% block content %}
       <div class="container">
           <h1>Welcome to Flask Monolith Example</h1>
           <p>Choose a service to get started:</p>
           <ul>
               <li><a href="{{ url_for('superapp.index') }}">SuperApp Service - Home</a></li>
               <li><a href="{{ url_for('superapp.echo', message='hello') }}">SuperApp Service - Echo 'hello'</a></li>
               <li><a href="{{ url_for('duperapp.index') }}">DuperApp Service - Home</a></li>
               <li><a href="{{ url_for('duperapp.echo', message='world') }}">DuperApp Service - Echo 'world'</a></li>
           </ul>
       </div>
   {% endblock %}
   ```

3. **Run and Test**:
   - Restart your Flask application and test the new endpoints to ensure they are working as expected.

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions that improve the clarity, functionality, or structure of this example are welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.