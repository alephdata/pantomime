# pantomime

[![build](https://github.com/alephdata/pantomime/actions/workflows/build.yml/badge.svg)](https://github.com/alephdata/pantomime/actions/workflows/build.yml)

``pantomime`` is a small library that handles the parsing and normalisation
of internet MIME types in Python. This can be useful to normalise invalid,
or misformatted MIME types emitted by remote web servers.

## Usage

The simplest use is to normalise a MIME type:

```python
from pantomime import normalize_mimetype

assert normalize_mimetype('TEXT/PLAIN') == 'text/plain'
assert normalize_mimetype('plain/text') == 'text/plain'
assert normalize_mimetype(None) == 'application/octet-stream'
assert normalize_mimetype('') == 'application/octet-stream'
```

Internally, `pantomime` uses a `MIMEType` object to handle parsing. It can
be used to access more specific information, like human readable labels:

```python
from pantomime import parse_mimetype

parsed = parse_mimetype('text/plain')
assert parsed.family == 'text'
assert parsed.subtype == 'plain'
assert parsed.label == 'Plain text'
```

## Open issues

* Internationalisation, i.e. make the human-readable labels available in
  multiple languages.
* Expand replacements for specific MIME types.

## License

Licensed under MIT terms, see the ``LICENSE`` file included in this repository.