from flask import abort, render_template, url_for

from newsapp.config import Config
from newsapp.main import bp
from newsapp.main.pagination import pagination
from newsapp.models.article import Article


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/<category>/<int:number>')
def news(category: str, number: int):
    if number < 1 or number > Article.page_count(category):
        abort(404)
    if category not in Config.CATEGORIES:
        abort(404)

    try:
        articles = Article.query.filter_by(category=category) \
            .order_by(Article.date) \
            .paginate(page=number, per_page=5).items
        articles = [dict(article) for article in articles]
        return render_template('news.html',
                               articles=articles,
                               pagination=pagination(category, number))
    except Exception as ex:
        bp.logger.info(ex)
        abort(500)
