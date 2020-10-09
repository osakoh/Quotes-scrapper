import requests

from pages.quotes_page import QuotesPage
"""
Retrieves a tag and extracts a quote information from that tag.
"""

# gets the entire HTML page
page_content = requests.get('http://quotes.toscrape.com/').content

# creates an object of the BeautifulSoup(page, 'html.parser')
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)

# print(page.quotes)