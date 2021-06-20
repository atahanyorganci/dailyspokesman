import click
from flask import Flask, current_app

from newsapp.config import Config
from newsapp.models import db, migrate
from newsapp.models.article import Article
from worker.tasks import update_news


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

    @app.shell_context_processor
    def shell_context():
        return {'app': app, 'db': db, 'Article': Article}

    @app.cli.command('scrape', help='Scrapes news from given category.')
    @click.argument('category')
    def scrape(category):
        categories = current_app.config['CATEGORIES']
        if category not in categories:
            categories = ", ".join(key for key in categories.keys())
            print(f'Unknown category, available categories: {categories}')
            return

        update_news(category)

    return app
