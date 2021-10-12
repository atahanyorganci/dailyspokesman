from datetime import datetime
from typing import Any

from yarl import URL

from newsapp.config import Config
from newsapp.models.article import Article
from newsapp.scraper import NewsItem, ScrapeError, scrape


def get_category_url(category: str) -> URL:
    category_path = Config.CATEGORIES[category]["url"]
    return Config.SCRAPER_BASE_URL / category_path


def parse_category_page(category: str) -> set[NewsItem]:
    category_url = get_category_url(category)
    category_page = scrape(category_url)
    urls: set[URL] = set()

    for comp in category_page.findAll("div", {"class": "news-item"}):
        url = URL(comp.a["href"])
        slug = url.path.strip("/").split("/")[-1]
        serialno = slug.split("-")[-1]

        # URL paths containing "?_szc_galeri" are not valid articles
        if "?_szc_galeri" in url.path:
            continue

        # Check if Article with given serialno exists
        if Article.query.filter_by(serialno=int(serialno)).first():
            continue

        urls.add(NewsItem(url=url, slug=slug, serialno=serialno, category=category))
    return urls


def parse_news_item(news_item: NewsItem) -> dict[str, Any]:
    page = scrape(news_item.url)
    article = page.find("article")

    if article is None:
        raise ScrapeError(f"{news_item} doesn't contain article element.")
    parsed = {}

    # Article content
    parsed["title"] = article.h1.text
    parsed["subtitle"] = article.h2.text
    parsed["content"] = " ".join([p.text for p in article.findAll("p")])

    # Link info
    parsed["category"] = news_item.category
    parsed["link"] = str(news_item.url)
    parsed["serialno"] = int(news_item.slug.split("-")[-1])

    # Parse article date
    meta_date = article.findAll("span", {"class": "content-meta-date"})[-1]
    date_str = meta_date.time["datetime"]
    parsed["date"] = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
    return parsed
