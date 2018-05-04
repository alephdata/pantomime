import unittest

from celestial import normalize_extension


class ExtensionTest(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(normalize_extension('.doc'), 'doc')
        self.assertEqual(normalize_extension(None), None)
        self.assertEqual(normalize_extension(''), None)
        self.assertEqual(normalize_extension('bla.doc'), 'doc')
        self.assertEqual(normalize_extension('bla.DOC'), 'doc')
        self.assertEqual(normalize_extension('bla.DO C'), 'doc')
        self.assertEqual(normalize_extension('bla.  DOC  '), 'doc')

        self.assertEqual(normalize_extension('TXT'), 'txt')
        self.assertEqual(normalize_extension('.TXT'), 'txt')
        self.assertEqual(normalize_extension('foo.txt'), 'txt')
        self.assertEqual(normalize_extension('foo..TXT'), 'txt')
        self.assertEqual(normalize_extension('.HTM,L'), 'html')
