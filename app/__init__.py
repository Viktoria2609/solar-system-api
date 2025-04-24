from flask import Flask
from .db import db, migrate
from .models import planet
from .routes.planet_routes import planet_list_bp


def create_app(test_config=None):
    app = Flask(__name__)

    
    app.register_blueprint(planet_list_bp)

    return app
