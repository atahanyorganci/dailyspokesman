from datetime import datetime
from typing import Set, Dict

from newsapp.config import Config
from newsapp.models.article import Article
from newsapp.scraper import Scraper


def get_category_url(category: str) -> str:
    url = Config.CATEGORIES[category]["url"]
    return f"{Config.SCRAPER_BASE_URL}{url}"


def parse_links(category: str) -> Set[str]:
    links = set()
    with Scraper(get_category_url(category)) as page:
        for comp in page.findAll("div", {"class": "listed-box"}):
            link = comp.a["href"]
            serialno = link.split("-")[-1][:-1]
            try:
                if (
                    not Article.query.filter_by(serialno=int(serialno)).first()
                    and "?_szc_galeri" not in link
                ):
                    links.add(link)
            except Exception as ex:
                links.add(link)
                print(f"{type(ex)} exception has occured.\n{ex}")
    return links


def parse_news(link: str, category: str) -> Dict[str, str]:
    parsed = {}
    with Scraper(link) as page:
        header = page.find("div", {"class": "content-head"})
        body = page.find("div", {"class": "content-element"})
        parsed["title"] = header.h1.text
        parsed["subtitle"] = header.h2.text
        parsed["content"] = " ".join([p.text for p in body.findAll("p")])
        parsed["link"] = link
        parsed["serialno"] = int(link.split("-")[-1][:-1])
        parsed["category"] = category

        date = header.find("div", {"class": "date-time"})
        date_str = date.text[14:].strip()
        parsed["date"] = datetime.strptime(date_str, "%H:%M, %d/%m/%Y")
    return parsed
