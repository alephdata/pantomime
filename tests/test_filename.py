import unittest

from pantomime.filename import FileName


class FileNameTest(unittest.TestCase):
    def test_none_filename(self):
        fn = FileName(None)
        self.assertEqual(fn.file_name, None)
        self.assertEqual(fn.extension, None)
        self.assertFalse(fn.has_extension)
        self.assertEqual(fn.safe(), "data")

    def test_normal_filename(self):
        fn = FileName("testing .doc")
        self.assertEqual(fn.file_name, "testing .doc")
        self.assertEqual(fn.extension, "doc")
        self.assertTrue(fn.has_extension)
        self.assertEqual(fn.safe(), "testing.doc")
        self.assertEqual(fn.safe("xls"), "testing.xls")

    def test_no_ext_filename(self):
        fn = FileName("testing xxx")
        self.assertEqual(fn.extension, None)
        self.assertFalse(fn.has_extension)
        self.assertEqual(fn.safe(), "testing_xxx")
        self.assertEqual(fn.safe("doc"), "testing_xxx.doc")
