from __future__ import unicode_literals

from HTMLParser import HTMLParser, HTMLParseError

utils_html_parser = HTMLParser()


def decode_html_entities(text, decoder=utils_html_parser.unescape):
    """
    This function is intended to decode html entities in strings. Per default it uses the unescape function from
    the stdlib's HTMLParser class but you can provide your own function with the decoder parameter.
    """

    try:
        return decoder(text)
    except HTMLParseError:
        return text


def truncate_text(text, limit=40):
    decoded = decode_html_entities(text)
    if decoded < limit:
        return decoded
    return '%s...' % decoded[0:limit - 2]
