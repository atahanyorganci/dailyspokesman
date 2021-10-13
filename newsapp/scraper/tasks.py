from logging import Logger

from newsapp.models import db
from newsapp.models.article import Article
from newsapp.scraper.parser import parse_category_page, parse_news_item


def update_news(category: str, *, logger: Logger) -> int:
    news_items = parse_category_page(category)
    logger.info(f"Found {len(news_items)} articles in {category.upper()} category.")
    for news_item in news_items:
        parsed = parse_news_item(news_item)
        article = Article(**parsed)
        db.session.add(article)
        logger.info(f"Article saved: {article}")
    db.session.commit()
    logger.info(f"Updated {category.upper()}.")

    return len(news_items)
