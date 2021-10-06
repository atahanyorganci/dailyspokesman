from decouple import config


def get_database_url() -> str:
    return config("DATABASE_URL").replace("postgres", "postgresql")


class Config:
    SECRET_KEY = config("SECRET_KEY", default="my-secret-key")
    DATABASE_URL = get_database_url()
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    REDIS_URL = config("REDIS_URL")
    REDIS_TLS_URL = config("REDIS_TLS_URL", default=None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CATEGORIES = {
        "headlines": {"display": "Headlines", "url": "gundem"},
        "world": {"display": "World", "url": "dunya"},
        "economy": {"display": "Economy", "url": "ekonomi"},
    }
    SCRAPER_BASE_URL = "https://www.sozcu.com.tr/kategori/"
    ARTICLE_PER_PAGE = 5
