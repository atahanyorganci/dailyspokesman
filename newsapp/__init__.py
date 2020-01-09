from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from newsapp.config import Config

db = SQLAlchemy()
migrate = Migrate()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(config_name=Config):
    # Flask application
    app = Flask(__name__)
    app.config.from_object(config_name)

    # Flask Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    celery.conf.update(app.config)

    # Blueprints
    from newsapp.errors import bp as errors
    from newsapp.main import bp as main

    app.register_blueprint(errors)
    app.register_blueprint(main)

    return app
