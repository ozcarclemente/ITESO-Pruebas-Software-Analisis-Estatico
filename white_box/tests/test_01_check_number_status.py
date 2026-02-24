"""
White-box unittest for check_number_status function.
"""

import unittest

from white_box.class_exercises import check_number_status


class TestCheckNumberStatus(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_check_number_status_positive(self):
        """
        Checks if a number is positive.
        """
        self.assertEqual(check_number_status(3), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if a number is negative.
        """
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if a number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_status_positive_float(self):
        """
        Checks if a positive float is identified as positive.
        """
        self.assertEqual(check_number_status(0.1), "Positive")

    def test_check_number_status_negative_float(self):
        """
        Checks if a negative float is identified as negative.
        """
        self.assertEqual(check_number_status(-0.1), "Negative")

    def test_check_number_status_large_values(self):
        """
        Checks very large positive and negative values.
        """
        self.assertEqual(check_number_status(10**18), "Positive")
        self.assertEqual(check_number_status(-(10**18)), "Negative")
