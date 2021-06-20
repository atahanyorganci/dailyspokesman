from flask import Flask

from newsapp.config import Config
from newsapp.models import db, migrate


def create_app(config_name=Config):
    # Flask application
    app = Flask(__name__)
    app.config.from_object(config_name)

    # Flask Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from newsapp.errors import bp as errors
    from newsapp.main import bp as main
    from newsapp.api import bp as api

    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(api)

    return app
