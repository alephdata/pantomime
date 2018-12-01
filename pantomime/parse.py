from cgi import parse_header
from normality import stringify
from normality.encoding import normalize_encoding

from pantomime.types import DEFAULT, LABELS
from pantomime.mappings import REPLACE


class MIMEType(object):
    __slots__ = ['family', 'subtype', 'params', 'name', 'normalized']

    SEP = '/'

    def __init__(self, family, subtype, params=None):
        self.family = family
        self.subtype = subtype
        self.name = None
        if self.family is not None and self.subtype is not None:
            self.name = self.SEP.join((self.family, self.subtype))
        self.normalized = REPLACE.get(self.name, self.name)
        self.params = params or {}

    @property
    def label(self):
        if self.normalized in LABELS:
            return LABELS.get(self.normalized)
        if self.subtype is not None:
            label = self.subtype.lstrip('x')
            label = label.replace('-', ' ')
            label = label.replace('.', ' ')
            return label.strip()

    @property
    def charset(self):
        charset = self.params.get('charset')
        return normalize_encoding(charset, default=None)

    @classmethod
    def split(cls, mime_type):
        if mime_type is None or cls.SEP not in mime_type:
            return None, None
        family, subtype = (stringify(p) for p in mime_type.split(cls.SEP, 1))
        if family is None or subtype is None:
            return None, None
        return family.lower(), subtype.lower()

    @classmethod
    def parse(cls, mime_type, default=None):
        mime_type = stringify(mime_type)
        params = None
        if mime_type is not None:
            mime_type, params = parse_header(mime_type)

        family, subtype = cls.split(mime_type)
        if family is None:
            family, subtype = cls.split(default)
        return cls(family, subtype, params=params)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name or DEFAULT

    def __repr__(self):
        return self.name
