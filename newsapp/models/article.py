import math
from datetime import datetime
from typing import Optional

from newsapp.config import Config
from newsapp.models import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_no = db.Column(db.Integer, nullable=False, unique=True)
    category = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

    @property
    def short_title(self):
        return self.title if len(self.title) < 50 else f"{self.title[:47]}..."

    def __repr__(self):
        return (
            f'<Article title="{self.short_title}"'
            f", serial_no={self.serial_no}"
            f", category={self.category}>"
        )

    def __iter__(self):
        yield "title", self.title
        yield "subtitle", self.subtitle
        yield "date", self.date.strftime("%d.%m.%y %H:%M")
        yield "content", self.content
        yield "url", self.url

    @classmethod
    def page_count(cls, category: str):
        count = cls.query.filter_by(category=category).count()
        return math.ceil(count / Config.ARTICLE_PER_PAGE)

    @classmethod
    def get_recent(cls, *, category: Optional[str] = None, limit: int = 10):
        query = cls.query.order_by(cls.date.desc())
        if category:
            query = query.filter_by(category=category)
        query = query.limit(limit)
        return query
