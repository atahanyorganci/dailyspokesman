import math

from flask import abort, render_template, url_for

from newsapp import app
from newsapp.models import Article


def article_to_dict(article: Article) -> dict:
    return {
        'title': article.title,
        'subtitle': article.subtitle,
        'date': article.date.strftime('%d.%m.%y %H:%M'),
        'content': article.content,
        'link': article.link
    }


def pagination(page: str, number: int) -> dict:
    count = Article.query.filter_by(category=page).count()
    page_count = math.ceil(count / 5)
    out = {}
    if number == 1:
        out['prev'] = ''
        out['labels'] = [(i, url_for('news', page=page, number=i))
                         for i in range(1, 4)]
        out['next'] = url_for('news', page=page, number=number + 1)
    elif number == page_count:
        out['prev'] = url_for('news', page=page, number=number - 1)
        out['labels'] = [(i, url_for('news', page=page, number=i))
                         for i in range(number - 2, number + 1)]
        out['next'] = ''
    else:
        out['prev'] = url_for('news', page=page, number=number-1)
        out['labels'] = [(i, url_for('news', page=page, number=i))
                         for i in range(number - 1, number + 2)]
        out['next'] = url_for('news', page=page, number=number+1)
    return out


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/<page>/<int:number>')
def news(page, number):
    if number < 1:
        abort(404)
    for category in app.config['CATEGORIES']:
        if page == category['api']:
            try:
                articles = Article.query.filter_by(category=category['url']).order_by(
                    Article.date).paginate(page=number, per_page=5).items
                articles = [article_to_dict(article) for article in articles]
                return render_template('news.html', articles=articles, pagination=pagination(category['url'], number))
            except:
                break
    abort(404)


@app.errorhandler(404)
def not_found_error(error):
    desc = {
        'title': '404 Not Found',
        'description': 'Tthe server can\'t find the requested resource.',
        'fix': 'Please check your request\'s URL.'
    }
    return render_template('error.html', error=desc), 404

@app.errorhandler(400)
def bad_request(error):
    desc = {
        'title': '400 Bad Request',
        'description': 'the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).',
        'fix': 'Please your request\'s syntax, framing, and routing.'
    }
    return render_template('error.html', error=desc), 400

@app.errorhandler(500)
def internal_error(error):
    desc = {
        'title': '500 Internal Server Error',
        'description': 'The server encountered an unexpected condition, and prevented it from fulfilling the request...',
        'fix': 'This is my fault.'
    }
    return render_template('500.html', error=desc), 500