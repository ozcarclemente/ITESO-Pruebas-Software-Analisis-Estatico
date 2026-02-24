"""
White-box unittest for validate_url function.
"""

import unittest

from white_box.class_exercises import validate_url


class TestValidateURL(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_valid_http_with_valid_length(self):
        """
        Checks valid URL starting with http:// and length <= 255.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_valid_https_with_valid_length(self):
        """
        Checks valid URL starting with https:// and length <= 255.
        """
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_invalid_missing_protocol(self):
        """
        Checks URL without http:// or https:// prefix.
        """
        self.assertEqual(validate_url("www.example.com"), "Invalid URL")

    def test_invalid_http_exceeds_length(self):
        """
        Checks http:// URL exceeding 255 characters.
        Should be invalid because length condition applies to http://.
        """
        long_url = "http://" + "a" * 250
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_valid_https_exceeds_length_due_to_precedence(self):
        """
        Checks https:// URL exceeding 255 characters.
        Due to operator precedence, https:// bypasses length validation.
        """
        long_url = "https://" + "a" * 300
        self.assertEqual(validate_url(long_url), "Valid URL")

    def test_invalid_empty_string(self):
        """
        Checks empty string input.
        """
        self.assertEqual(validate_url(""), "Invalid URL")
