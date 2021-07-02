import click
from flask import Flask, current_app
from tabulate import tabulate

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

    @app.cli.command('scrape', help='Scrape news from given category.')
    @click.argument('category')
    def scrape(category):
        allowed = {'all', *current_app.config['CATEGORIES']}
        if category not in allowed:
            allowed = ', '.join(key for key in allowed.keys())
            print(f'Unknown category, allowed: {allowed}')
            return

        if category == 'all':
            for category in current_app.config['CATEGORIES']:
                update_news(category)
        else:
            update_news(category)

    @app.cli.group('article', help='Interact with articles in the db.')
    def article():
        pass

    @article.command('describe', help='Print info about saved articles')
    def describe():
        data = [[
            category.title(),
            Article.query.filter_by(category=category).count()
        ] for category in current_app.config['CATEGORIES']]
        print(tabulate(data, headers=['Category', 'Count'], tablefmt='presto'))

    @article.command('display', help='Display latest Article objects from db.')
    @click.argument('category')
    @click.option('--count', default=20, type=int)
    def display(category, count):
        allowed = {'all', *current_app.config['CATEGORIES']}
        if category not in allowed:
            allowed = ', '.join(key for key in allowed.keys())
            print(f'Unknown category, allowed: {allowed}')
            return

        if category == 'all':
            articles = Article.query.order_by(Article.date).limit(count)
            data = [[
                article.serialno, article.short_title, article.date,
                article.category
            ] for article in articles]
            print(
                tabulate(data,
                         headers=['Serial No', 'Title', 'Date', 'Category'],
                         tablefmt='presto'))
        else:
            articles = Article.query.filter_by(category=category).order_by(
                Article.date).limit(count)
            data = [[
                article.serialno,
                article.short_title,
                article.date,
            ] for article in articles]
            print(
                tabulate(data,
                         headers=['Serial No', 'Title', 'Date'],
                         tablefmt='presto'))

    return app
