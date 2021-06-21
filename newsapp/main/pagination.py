import math

from flask import url_for

from newsapp.models.article import Article


def pagination(category: str, number: int) -> dict:
    page_count = Article.page_count(category)

    out = {}
    if number == 1:
        out['prev'] = ''
        out['labels'] = [(i, url_for('main.news', category=category, number=i))
                         for i in range(1, 4)]
        out['next'] = url_for('main.news',
                              category=category,
                              number=number + 1)
    elif number == page_count:
        out['prev'] = url_for('main.news',
                              category=category,
                              number=number - 1)
        out['labels'] = [(i, url_for('main.news', category=category, number=i))
                         for i in range(number - 2, number + 1)]
        out['next'] = ''
    else:
        out['prev'] = url_for('main.news',
                              category=category,
                              number=number - 1)
        out['labels'] = [(i, url_for('main.news', category=category, number=i))
                         for i in range(number - 1, number + 2)]
        out['next'] = url_for('main.news',
                              category=category,
                              number=number + 1)
    return out
