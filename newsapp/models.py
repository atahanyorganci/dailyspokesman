from datetime import datetime

from newsapp import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serialno = db.Column(db.Integer, nullable=False, unique=True)
    category = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Article serial={self.serialno} category={self.category}>'
