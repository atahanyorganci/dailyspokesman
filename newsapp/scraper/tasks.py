from newsapp.scraper.parser import parse_links, parse_news
from newsapp.models import db
from newsapp.models.article import Article


def update_news(category: str, *, logger) -> int:
    links = parse_links(category)
    logger.info(f'Found {len(links)} articles in {category.upper()} category.')
    for link in links:
        news = parse_news(link, category)
        article = Article.from_dict(news)
        db.session.add(article)
        logger.info(f'Article saved: {article}')
    db.session.commit()
    logger.info(f'Updated {category.upper()}.')

    return len(links)
