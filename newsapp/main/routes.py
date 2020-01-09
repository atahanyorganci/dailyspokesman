from flask import abort, render_template, url_for

from newsapp.config import Config
from newsapp.main import bp
from newsapp.main.pagination import pagination
from newsapp.models import Article


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/<category>/<int:number>')
def news(category, number):
    if number < 1:
        abort(404)
    for config in Config.CATEGORIES:
        if category == config['api']:
            name = config['url']
            try:
                articles = Article.query.filter_by(category=name).order_by(
                    Article.date).paginate(page=number, per_page=5).items
                articles = [dict(article) for article in articles]
                return render_template('news.html', articles=articles, pagination=pagination(name, number))
            except Exception as ex:
                print(ex)
                break
    abort(404)
