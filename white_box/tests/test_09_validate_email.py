"""
White-box unittest for validate_email function.
"""

import unittest

from white_box.class_exercises import validate_email


class TestValidateEmail(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_valid_email_min_length_boundary(self):
        """
        Checks a valid email with minimum allowed length (5 characters).
        """
        self.assertEqual(validate_email("a@b.c"), "Valid Email")

    def test_valid_email_max_length_boundary(self):
        """
        Checks a valid email with maximum allowed length (50 characters).
        """
        email = "a" * 38 + "@test.com"  # Total length = 50
        self.assertEqual(validate_email(email), "Valid Email")

    def test_invalid_email_too_short(self):
        """
        Checks an email shorter than minimum length.
        """
        self.assertEqual(validate_email("a@b"), "Invalid Email")

    def test_invalid_email_too_long(self):
        """
        Checks an email longer than maximum length.
        """
        email = "a" * 50 + "@test.com"  # Length > 50
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_invalid_email_missing_at_symbol(self):
        """
        Checks an email missing '@' symbol.
        """
        self.assertEqual(validate_email("abc.test.com"), "Invalid Email")

    def test_invalid_email_missing_dot(self):
        """
        Checks an email missing '.' symbol.
        """
        self.assertEqual(validate_email("abc@testcom"), "Invalid Email")

    def test_invalid_email_missing_at_and_dot(self):
        """
        Checks an email missing both '@' and '.'.
        """
        self.assertEqual(validate_email("abcdef"), "Invalid Email")
