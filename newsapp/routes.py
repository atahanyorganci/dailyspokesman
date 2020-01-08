import math
from pprint import pformat

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


def pagination(category: str, number: int) -> dict:
    count = Article.query.filter_by(category=category).count()
    page_count = math.ceil(count / 5)
    out = {}
    if number == 1:
        out['prev'] = ''
        out['labels'] = [(i, url_for('news', category=category, number=i)) for i in range(1, 4)]
        out['next'] = url_for('news', category=category, number=number + 1)
    elif number == page_count:
        out['prev'] = url_for('news', category=category, number=number - 1)
        out['labels'] = [(i, url_for('news', category=category, number=i)) for i in range(number - 2, number + 1)]
        out['next'] = ''
    else:
        out['prev'] = url_for('news', category=category, number=number-1)
        out['labels'] = [(i, url_for('news', category=category, number=i)) for i in range(number - 1, number + 2)]
        out['next'] = url_for('news', category=category, number=number+1)
    return out


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/<category>/<int:number>')
def news(category, number):
    if category not in app.config['CATEGORIES'] or number < 1:
        abort(404)
    try:
        articles = Article.query.filter_by(category=category).order_by(
            Article.date).paginate(page=number, per_page=5).items
        articles = [article_to_dict(article) for article in articles]
        print(url_for('news', category='ekonomi', number=1))
        return render_template('news.html', articles=articles, pagination=pagination(category, number))
    except:
        abort(404)
