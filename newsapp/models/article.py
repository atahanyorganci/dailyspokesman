from datetime import datetime
import math

from newsapp.models import db
from newsapp.config import Config


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serialno = db.Column(db.Integer, nullable=False, unique=True)
    category = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Article serial={self.serialno} category={self.category}>'

    def __iter__(self):
        yield 'title', self.title
        yield 'subtitle', self.subtitle
        yield 'date', self.date.strftime('%d.%m.%y %H:%M')
        yield 'content', self.content
        yield 'link', self.link

    @classmethod
    def page_count(cls, category: str):
        count = cls.query.filter_by(category=category).count()
        return math.ceil(count / Config.ARTICLE_PER_PAGE)
