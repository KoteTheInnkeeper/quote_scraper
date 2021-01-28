class QuoteLocators:
    """
        Given a quote in the page (a div.quote tag), this locators are unique enough to extract the information we
        want.

        The idea es to make the parser access each quote individually and, with this locators, find what we want.
    """
    AUTHOR = 'small.author' # only one element
    CONTENT = 'span.text'   # only one element
    TAGS = 'div.tags a.tag' # multiple elements
