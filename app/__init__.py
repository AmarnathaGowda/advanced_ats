from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    
    # Initialize Swagger with a simple configuration
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }
    Swagger(app, config=swagger_config)
    
    # Import and register the routes blueprint
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
