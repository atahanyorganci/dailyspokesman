from flask import abort, jsonify

from newsapp.api import bp
from newsapp.config import Config
from newsapp.models.article import Article


@bp.route('/<category>')
def info(category):
    for config in Config.CATEGORIES:
        if category == config['api']:
            name = config['url']
            count = Article.query.filter_by(category=name).count()
            return jsonify({
                'count': count,
                'display': config['display']})
    abort(400)


@bp.route('/<category>/<int:number>')
def single_article(category, number):
    if number < 1:
        abort(400)
    for config in Config.CATEGORIES:
        if category == config['api']:
            name = config['url']
            try:
                count = Article.query.filter_by(category=name).count()
                if number > count:
                    break
                article = Article.query.filter_by(
                    category=name).order_by(Article.date)[number - 1]
                return jsonify(dict(article))
            except:
                break
    abort(400)
