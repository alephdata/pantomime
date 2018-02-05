import unittest

from celestial import parse_mime, normalize_mime, DEFAULT


class MIMETest(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(normalize_mime('TEXT/ PLAIN'), 'text/plain')
        self.assertEqual(normalize_mime('TEXT/'), 'text/other')
        self.assertEqual(normalize_mime('1'), DEFAULT)
        self.assertEqual(normalize_mime(None), DEFAULT)

    def test_parse(self):
        parsed = parse_mime('text/plain')
        self.assertEqual(parsed.charset, None)
        self.assertEqual(parsed.family, 'text')
        self.assertEqual(parsed.subtype, 'plain')
        self.assertEqual('%s' % parsed, 'text/plain')
        self.assertEqual('%r' % parsed, 'text/plain')
        parsed = parse_mime('text/plain; charset=cp1251')
        self.assertEqual(parsed.charset, 'cp1251')
