import os
from banal import decode_path
from normality import slugify

from pantomime.parse import MIMEType
from pantomime.types import DEFAULT, PLAIN


def parse_mimetype(text, default=DEFAULT):
    """Parse a MIME type into a structured object."""
    return MIMEType.parse(text, default=default)


def normalize_mimetype(text, default=DEFAULT):
    """Normalize the spelling of a MIME type."""
    return parse_mimetype(text, default=default).normalized


def useful_mimetype(text):
    """Check to see if the given mime type is a MIME type
    which is useful in terms of how to treat this file.
    """
    if text is None:
        return False
    mimetype = normalize_mimetype(text)
    return mimetype not in [DEFAULT, PLAIN, None]


def normalize_extension(extension):
    """Normalise a file name extension."""
    extension = decode_path(extension)
    if extension is None:
        return
    if extension.startswith('.'):
        extension = extension[1:]
    if '.' in extension:
        _, extension = os.path.splitext(extension)
    extension = slugify(extension, sep='')
    if extension is None:
        return
    if len(extension):
        return extension
