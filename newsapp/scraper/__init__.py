from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
from yarl import URL


class ScrapeError(Exception):
    pass


def scrape(url: URL) -> BeautifulSoup:
    response = requests.get(str(url))
    if not response.ok:
        raise ScrapeError(f"Request to {url} failed with status {response.status_code}")
    return BeautifulSoup(response.text, "html.parser")


@dataclass(frozen=True)
class NewsItem:
    url: URL
    slug: str
    serialno: str
    category: str

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, NewsItem):
            return False
        return self.url == o.url

    def __hash__(self) -> int:
        return hash(str(self.url))
