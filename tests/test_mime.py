import unittest

from celestial import parse_mimetype, normalize_mimetype, DEFAULT


class MIMETest(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(normalize_mimetype('TEXT/ PLAIN'), 'text/plain')
        self.assertEqual(normalize_mimetype('TEXT/'), 'text/other')
        self.assertEqual(normalize_mimetype('1'), DEFAULT)
        self.assertEqual(normalize_mimetype(None), DEFAULT)

    def test_parse(self):
        parsed = parse_mimetype('text/plain')
        self.assertEqual(parsed.charset, None)
        self.assertEqual(parsed.family, 'text')
        self.assertEqual(parsed.subtype, 'plain')
        self.assertEqual('%s' % parsed, 'text/plain')
        self.assertEqual('%r' % parsed, 'text/plain')
        parsed = parse_mimetype('text/plain; charset=cp1251')
        self.assertEqual(parsed.charset, 'cp1251')
        parsed = parse_mimetype('text/plain; charset=banana')
        self.assertEqual(parsed.charset, None)
