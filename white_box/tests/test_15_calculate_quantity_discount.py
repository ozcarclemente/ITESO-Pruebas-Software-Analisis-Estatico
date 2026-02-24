"""
White-box unittest for calculate_quantity_discount function.
"""

import unittest

from white_box.class_exercises import calculate_quantity_discount


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_no_discount_lower_boundary(self):
        """
        Checks lower boundary for 'No Discount' (quantity = 1).
        """
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_no_discount_upper_boundary(self):
        """
        Checks upper boundary for 'No Discount' (quantity = 5).
        """
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_five_percent_discount_lower_boundary(self):
        """
        Checks lower boundary for '5% Discount' (quantity = 6).
        """
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_five_percent_discount_upper_boundary(self):
        """
        Checks upper boundary for '5% Discount' (quantity = 10).
        """
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_ten_percent_discount_above_range(self):
        """
        Checks quantity greater than 10 for '10% Discount'.
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_ten_percent_discount_zero_quantity(self):
        """
        Checks quantity below defined ranges (quantity = 0).
        """
        self.assertEqual(calculate_quantity_discount(0), "10% Discount")

    def test_ten_percent_discount_negative_quantity(self):
        """
        Checks negative quantity values.
        """
        self.assertEqual(calculate_quantity_discount(-3), "10% Discount")
