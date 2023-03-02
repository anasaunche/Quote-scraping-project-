from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotesPagesLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotesPagesLocators.QUOTE)]
