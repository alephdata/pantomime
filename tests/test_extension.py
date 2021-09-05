import unittest

from pantomime.filename import normalize_extension
from pantomime.filename import mimetype_extension as mime_ext


class ExtensionTest(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_extension(".doc"), "doc")
        self.assertEqual(normalize_extension(None), None)
        self.assertEqual(normalize_extension(""), None)
        self.assertEqual(normalize_extension("bla.doc"), "doc")
        self.assertEqual(normalize_extension("bla.DOC"), "doc")
        self.assertEqual(normalize_extension("bla.DO C"), "doc")
        self.assertEqual(normalize_extension("bla.  DOC  "), "doc")

        self.assertEqual(normalize_extension("TXT"), "txt")
        self.assertEqual(normalize_extension(".TXT"), "txt")
        self.assertEqual(normalize_extension("foo.txt"), "txt")
        self.assertEqual(normalize_extension("foo..TXT"), "txt")
        self.assertEqual(normalize_extension(".HTM,L"), "html")

    def test_mimetype_extension(self):
        self.assertEqual(mime_ext(None), None)
        self.assertEqual(mime_ext(""), None)
        self.assertEqual(mime_ext("bla"), None)
        self.assertEqual(mime_ext("application/pdf"), "pdf")
