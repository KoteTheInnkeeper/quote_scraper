from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)  # Here lies all the 'div.quote' tags. So we have a list of tags
        # containing the quotes.
        return [QuoteParser(e) for e in quote_tags] # We then pass each 'quote tags' to the 'QuoteParser'
    # QuoteParser was designed to work with each 'div.quote' tag and search, inside this individually, the info we want.
