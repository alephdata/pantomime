from celestial.parse import MIMEType
from celestial.types import DEFAULT, PLAIN


def parse_mimetype(text, default=DEFAULT):
    """Parse a MIME type into a structured object."""
    return MIMEType.parse(text, default=default)


def normalize_mimetype(text, default=DEFAULT):
    """Normalize the spelling of a MIME type."""
    return parse_mimetype(text, default=default).label


def useful_mimetype(text):
    """Check to see if the given mime type is a MIME type
    which is useful in terms of how to treat this file.
    """
    if text is None:
        return False
    mimetype = normalize_mimetype(text)
    return mimetype not in [DEFAULT, PLAIN, None]
