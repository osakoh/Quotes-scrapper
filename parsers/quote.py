from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    For extracting information(content, author, & tags) from a single quote(a single div)
    """

    def __init__(self, parent):
        """
        :param parent: represents a single div tag from the page(website)
        """
        self.parent = parent  # single div

    def __repr__(self):
        return "<Quote {}, by {}>".format(self.content, self.author)

    def __str__(self):
        return "Quote: {}\nAuthor: {}\nTags: {}\n".format(self.content, self.author, self.tags)

    # method becomes a property(not an action) of this class i.e this method can be called without the parenthesis()
    @property
    def content(self):
        """
        :return: the content within the parent(div) tag
        """
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string  # retrieves the text

    # method becomes a property(not an action) of this class i.e this method can be called without the parenthesis()
    @property
    def author(self):
        """
        :return: the name of the author within the parent(div) tag
        """
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string  # retrieves the author's name

    # method becomes a property(not an action) of this class i.e this method can be called without the parenthesis()
    @property
    def tags(self):
        """
        :return: all the tags within the parent(div) tag
        """
        locator = QuoteLocators.TAGS
        return [tag.string for tag in self.parent.select(locator)]  # retrieves the tags in a 'list' format
