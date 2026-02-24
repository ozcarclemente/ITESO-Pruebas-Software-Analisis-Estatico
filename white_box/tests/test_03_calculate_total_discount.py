"""
White-box unittest for calculate_total_discount function.
"""

import unittest

from white_box.class_exercises import calculate_total_discount


class TestCalculateTotalDiscount(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_calculate_total_discount_no_discount(self):
        """
        Checks if the total discount is 0 when no discounts apply.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_10_percent(self):
        """
        Checks if the total discount is 10% when the price is above $100 and below $500.
        """
        self.assertEqual(calculate_total_discount(150), 15)

    def test_calculate_total_discount_20_percent(self):
        """
        Checks if the total discount is 20% when the price is above $500.
        """
        self.assertEqual(calculate_total_discount(700), 140)

    def test_calculate_total_discount_exact_boundaries(self):
        """
        Checks boundary values at 100 and 500.
        """
        self.assertEqual(calculate_total_discount(100), 10)
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_just_below_and_zero_negative(self):
        """
        Checks values just below the threshold, zero and negative amounts.
        """
        self.assertEqual(calculate_total_discount(99.99), 0)
        self.assertEqual(calculate_total_discount(0), 0)
        self.assertEqual(calculate_total_discount(-20), 0)

    def test_calculate_total_discount_fractional_and_large(self):
        """
        Checks fractional totals and large amounts; use approximate checks for floats.
        """
        self.assertAlmostEqual(calculate_total_discount(250.5), 25.05, places=2)
        self.assertAlmostEqual(calculate_total_discount(500.01), 0.2 * 500.01, places=3)
        self.assertEqual(calculate_total_discount(1000), 200)
