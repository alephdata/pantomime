import os
from banal import decode_path
from mimetypes import guess_extension
from normality import slugify, safe_filename

from pantomime.mime import normalize_mimetype
from pantomime.types import DEFAULT


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


def mimetype_extension(mime_type):
    """Infer a possible extension from a MIME type."""
    mime_type = normalize_mimetype(mime_type)
    if mime_type == DEFAULT:
        return None
    extension = guess_extension(mime_type)
    return normalize_extension(extension)


class FileName(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.base, self.extension = None, None
        if file_name is not None:
            self.base, ext = os.path.splitext(file_name)
            self.extension = normalize_extension(ext)
        self.has_extension = self.extension is not None

    def safe(self, extension=None):
        ext = extension or self.extension
        default = 'data.%s' % ext if ext else 'data'
        return safe_filename(self.file_name, default=default, extension=ext)

    def __str__(self):
        return self.file_name

    def __repr__(self):
        return self.safe()
