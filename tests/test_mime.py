import unittest

from pantomime import parse_mimetype, normalize_mimetype, DEFAULT
from pantomime import useful_mimetype


class MIMETest(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_mimetype("TEXT/ PLAIN"), "text/plain")
        self.assertEqual(normalize_mimetype("TEXT/"), DEFAULT)
        self.assertEqual(normalize_mimetype("1"), DEFAULT)
        self.assertEqual(normalize_mimetype("1", default=None), None)
        self.assertEqual(normalize_mimetype(None), DEFAULT)

        PST = "application/VND.ms-outlook"
        self.assertEqual(normalize_mimetype(PST), PST.lower())

    def test_useful(self):
        self.assertFalse(useful_mimetype(None))
        self.assertFalse(useful_mimetype(DEFAULT))
        self.assertTrue(useful_mimetype("image/png"))

    def test_label(self):
        parsed = parse_mimetype("application/x-pudo-banana")
        self.assertEqual(parsed.label, "pudo banana")

    def test_parse(self):
        parsed = parse_mimetype("text/plain")
        self.assertEqual(parsed.charset, None)
        self.assertEqual(parsed.label, "Plain text")
        self.assertEqual(parsed.family, "text")
        self.assertEqual(parsed.subtype, "plain")
        self.assertEqual(parsed.normalized, "text/plain")
        self.assertEqual("%s" % parsed, "text/plain")
        self.assertEqual("%r" % parsed, "text/plain")
        parsed = parse_mimetype("text/plain; charset=cp1251")
        self.assertEqual(parsed.charset, "cp1251")
        parsed = parse_mimetype("text/plain; charset=banana")
        self.assertEqual(parsed.charset, "utf-8")

        self.assertEqual(parsed, parse_mimetype("text/plain"))

    def test_parse_rewrite(self):
        parsed = parse_mimetype("plain/text")
        self.assertEqual(parsed.normalized, "text/plain")
