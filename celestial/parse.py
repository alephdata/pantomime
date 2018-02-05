from six import text_type as text
from cgi import parse_header
from normality import stringify
from normality.encoding import normalize_encoding


class MIMEType(object):
    __slots__ = ['family', 'subtype', 'params', 'label']

    SEP = text('/')

    def __init__(self, family, subtype, params=None):
        self.family = self.normalize_part(family, text('application'))
        self.subtype = self.normalize_part(subtype, text('other'))
        self.params = params
        self.label = self.SEP.join((self.family, self.subtype))

    @property
    def charset(self):
        if self.params is None:
            return
        charset = self.params.get('charset')
        return normalize_encoding(charset, default=None)

    def normalize_part(self, part, default):
        part = stringify(part) or default
        part = part.strip().lower()
        return part

    @classmethod
    def parse(cls, mime_type, default):
        mime_type = stringify(mime_type) or default
        mime_type, params = parse_header(mime_type)
        if cls.SEP not in mime_type:
            mime_type = default
        family, subtype = mime_type.split(cls.SEP, 1)
        return cls(family, subtype, params=params)

    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label
