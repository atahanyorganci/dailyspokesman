from newsapp.config import Config
from newsapp.models import db
from newsapp.models.article import Article
from newsapp.util.parser import parse_links, parse_news


def update_news(category: str):
    links = parse_links(category)
    print(f'* Found {len(links)} links in {category.upper()} category.')
    for link in links:
        news = parse_news(link, category)
        a = Article(serialno=news['serialno'],
                    category=news['category'],
                    title=news['title'],
                    subtitle=news['subtitle'],
                    content=news['content'],
                    link=news['link'])
        db.session.add(a)
        db.session.commit()
        print(f"News acquired {news['title']}, {news['serialno']}")
