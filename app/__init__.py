from flask import Flask
from .db import db, migrate
from .models import planet, moon
from .routes.planet_routes import bp as planet_list_bp
from .routes.moon_routes import bp as moon_bp
import os


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    if test_config:
        
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planet_list_bp)
    app.register_blueprint(moon_bp)

    return app
