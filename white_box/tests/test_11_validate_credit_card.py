"""
White-box unittest for validate_credit_card function.
"""

import unittest

from white_box.class_exercises import validate_credit_card


class TestValidateCreditCard(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_valid_card_min_length(self):
        """
        Checks valid card with minimum allowed length (13 digits).
        """
        self.assertEqual(validate_credit_card("1" * 13), "Valid Card")

    def test_valid_card_max_length(self):
        """
        Checks valid card with maximum allowed length (16 digits).
        """
        self.assertEqual(validate_credit_card("1" * 16), "Valid Card")

    def test_invalid_card_too_short(self):
        """
        Checks card number shorter than 13 digits.
        """
        self.assertEqual(validate_credit_card("1" * 12), "Invalid Card")

    def test_invalid_card_too_long(self):
        """
        Checks card number longer than 16 digits.
        """
        self.assertEqual(validate_credit_card("1" * 17), "Invalid Card")

    def test_invalid_card_with_letters(self):
        """
        Checks card number containing non-digit characters.
        """
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")

    def test_invalid_card_with_special_characters(self):
        """
        Checks card number containing special characters.
        """
        self.assertEqual(validate_credit_card("1234-5678-9012"), "Invalid Card")

    def test_invalid_card_valid_length_non_digit(self):
        """
        Checks card number with valid length but containing non-digit characters.
        """
        self.assertEqual(validate_credit_card("1" * 15 + "a"), "Invalid Card")
