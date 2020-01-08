import requests
from bs4 import BeautifulSoup


class Scraper(object):
    def __init__(self, url: str) -> None:
        self.__url = url

    def __enter__(self) -> BeautifulSoup:
        try:
            with requests.get(self.__url) as resp:
                html = resp.text
        except Exception as ex:
            self.__exit__(type(ex), ex, __name__)
        else:
            self.status = resp.status_code
            self.soup = BeautifulSoup(html, 'html.parser')
            return self.soup

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        if type(exc_type) is Exception:
            raise exc_type(exc_value)