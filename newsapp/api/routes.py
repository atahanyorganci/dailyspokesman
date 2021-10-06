from flask import abort, jsonify

from newsapp.api import bp
from newsapp.config import Config
from newsapp.models.article import Article


@bp.route("/")
def index():
    info = {}
    for category in Config.CATEGORIES:
        info[category] = Article.query.filter_by(category=category).count()
    return jsonify(info)


@bp.route("/<category>")
def get_category(category: str):
    if category not in Config.CATEGORIES:
        abort(400)

    try:
        articles = (
            Article.query.filter_by(category=category)
            .order_by(Article.date.desc())
            .paginate(page=1, per_page=5)
            .items
        )
        return jsonify([dict(article) for article in articles])
    except Exception as ex:
        bp.logger.info(ex)
        abort(500)


@bp.route("/<category>/<int:number>")
def news(category: str, number: int):
    if category not in Config.CATEGORIES:
        abort(400)
    if number < 1 or number > Article.page_count(category):
        abort(404)

    try:
        articles = (
            Article.query.filter_by(category=category)
            .order_by(Article.date.desc())
            .paginate(page=number, per_page=5)
            .items
        )
        return jsonify([dict(article) for article in articles])
    except Exception as ex:
        bp.logger.info(ex)
        abort(500)
