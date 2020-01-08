import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'news.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
