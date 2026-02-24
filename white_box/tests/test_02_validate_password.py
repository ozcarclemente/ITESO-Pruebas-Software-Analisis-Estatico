"""
White-box unittest for validate_password function.
"""

import unittest

from white_box.class_exercises import validate_password


class TestValidatePassword(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_validate_password_valid(self):
        """
        Checks if a valid password is accepted.
        """
        self.assertTrue(validate_password("Valid123!@#$%&"))

    def test_validate_password_invalid(self):
        """
        Checks if an invalid password is rejected.
        """
        self.assertFalse(validate_password("invalid"))

    def test_validate_password_short(self):
        """
        Checks if a short password is rejected.
        """
        self.assertFalse(validate_password("Short1!"))

    def test_validate_password_min_length_valid(self):
        """
        Exactly 8 chars with required character classes should pass.
        """
        self.assertTrue(validate_password("Aaa1!aaa"))

    def test_validate_password_missing_uppercase(self):
        """
        Missing uppercase should fail.
        """
        self.assertFalse(validate_password("valid123!"))

    def test_validate_password_missing_lowercase(self):
        """
        Missing lowercase should fail.
        """
        self.assertFalse(validate_password("VALID123!"))

    def test_validate_password_missing_digit(self):
        """
        Missing digit should fail.
        """
        self.assertFalse(validate_password("Valid!!!"))

    def test_validate_password_missing_allowed_special(self):
        """
        Has a special character but not one from the allowed set -> fail.
        """
        self.assertFalse(validate_password("Valid123}"))
