from celestial.parse import MIMEType
from celestial.types import DEFAULT


def parse_mime(text, default=DEFAULT):
    """Parse a MIME type into a structured object."""
    return MIMEType.parse(text, default)


def normalize_mime(text, default=DEFAULT):
    """Normalize the spelling of a MIME type."""
    return parse_mime(text, default=default).label
