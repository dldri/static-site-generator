import unittest
from main import extract_title


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello World"
        title = extract_title(markdown)
        self.assertEqual(
            title,
            "Hello World"
        )

    def test_extract_title_exception(self):
        markdown = "## This is h2"
        self.assertRaises(LookupError, extract_title, markdown)
