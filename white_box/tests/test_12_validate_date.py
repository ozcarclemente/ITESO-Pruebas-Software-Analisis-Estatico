"""
White-box unittest for validate_date function.
"""

import unittest

from white_box.class_exercises import validate_date


class TestValidateDate(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_valid_date_lower_boundaries(self):
        """
        Checks lower boundary values for year, month, and day.
        """
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_valid_date_upper_boundaries(self):
        """
        Checks upper boundary values for year, month, and day.
        """
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_invalid_year_below_range(self):
        """
        Checks year below valid range.
        """
        self.assertEqual(validate_date(1899, 6, 15), "Invalid Date")

    def test_invalid_year_above_range(self):
        """
        Checks year above valid range.
        """
        self.assertEqual(validate_date(2101, 6, 15), "Invalid Date")

    def test_invalid_month_below_range(self):
        """
        Checks month below valid range.
        """
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_invalid_month_above_range(self):
        """
        Checks month above valid range.
        """
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_invalid_day_below_range(self):
        """
        Checks day below valid range.
        """
        self.assertEqual(validate_date(2000, 6, 0), "Invalid Date")

    def test_invalid_day_above_range(self):
        """
        Checks day above valid range.
        """
        self.assertEqual(validate_date(2000, 6, 32), "Invalid Date")

    def test_invalid_multiple_fields(self):
        """
        Checks multiple invalid fields simultaneously.
        """
        self.assertEqual(validate_date(1800, 15, 40), "Invalid Date")
