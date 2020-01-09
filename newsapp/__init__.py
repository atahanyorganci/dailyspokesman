from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from newsapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from newsapp import tasks

from newsapp.errors import bp as errors
from newsapp.main import bp as main

app.register_blueprint(errors)
app.register_blueprint(main)
