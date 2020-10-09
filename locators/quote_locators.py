class QuoteLocators:
    """
    For extracting information within a single quote
    """
    CONTENT = 'span.text'  # locates the content(quote) located within the 'div' tag from the quotes page(website)
    AUTHOR = 'small.author'  # locates the author within the small tag
    TAGS = 'div.tags a.tag'  # locate all the tags with the 'div' and 'a' tag
