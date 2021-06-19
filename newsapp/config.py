import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'news.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CATEGORIES = [
        {
            'url': 'gundem',
            'api': 'head',
            'display': 'Headlines',
        },
        {
            'url': 'dunya',
            'api': 'world',
            'display': 'World',
        },
        {
            'url': 'ekonomi',
            'api': 'econ',
            'display': 'Economy',
        },
    ]
    SCRAPPER_BASE_URL = 'https://www.sozcu.com.tr/kategori/'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERYBEAT_SCHEDULE = {
        f'update-news-{category["api"]}': {
            'task': 'newsapp.tasks.update_news',
            'schedule': 300.0,
            'args': (category['url'],)
        } for category in CATEGORIES
    }
