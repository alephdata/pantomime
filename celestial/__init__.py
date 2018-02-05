from celestial.parse import MIMEType
from celestial.types import DEFAULT


def parse_mimetype(text, default=DEFAULT):
    """Parse a MIME type into a structured object."""
    return MIMEType.parse(text, default)


def normalize_mimetype(text, default=DEFAULT):
    """Normalize the spelling of a MIME type."""
    return parse_mimetype(text, default=default).label
