from decouple import config
from yarl import URL


def get_database_url() -> str:
    return config("DATABASE_URL").replace("postgres", "postgresql")


class Config:
    SECRET_KEY = config("SECRET_KEY", default="my-secret-key")
    DATABASE_URL = get_database_url()
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CATEGORIES = {
        "headlines": {"display": "Headlines", "url": "gundem"},
        "world": {"display": "World", "url": "dunya"},
        "economy": {"display": "Economy", "url": "ekonomi"},
        "automotive": {"display": "Automotive", "url": "otomotiv"},
    }
    SCRAPER_BASE_URL = URL("https://www.sozcu.com.tr/kategori/")
    ARTICLE_PER_PAGE = 5
