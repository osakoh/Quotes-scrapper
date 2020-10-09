from bs4 import BeautifulSoup

from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    """
    For extracting information from the quotes page(website)
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        """
        :return: all the 'div' tags from the page(website)
        """
        locator = QuotesPageLocators.QUOTES  # locates all the 'divs' in the website
        quote_div_tags = self.soup.select(locator)
        # print(quote_div_tags)
        # gets the content, author and tags from the 'div' tags
        return [QuoteParser(e) for e in quote_div_tags]