"""
White-box unittest for calculate_shipping_cost function.
"""

import unittest

from white_box.class_exercises import calculate_shipping_cost


class TestCalculateShippingCost(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_small_package_all_lower_boundaries(self):
        """
        Checks first tier with minimum valid values.
        """
        self.assertEqual(calculate_shipping_cost(0.5, 5, 5, 5), 5)

    def test_small_package_upper_boundaries(self):
        """
        Checks first tier at upper boundary limits.
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package_lower_boundaries(self):
        """
        Checks second tier at lower boundaries.
        """
        self.assertEqual(calculate_shipping_cost(1.1, 11, 11, 11), 10)

    def test_medium_package_upper_boundaries(self):
        """
        Checks second tier at upper boundaries.
        """
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_large_package_due_to_weight(self):
        """
        Checks third tier when weight exceeds medium range.
        """
        self.assertEqual(calculate_shipping_cost(6, 20, 20, 20), 20)

    def test_large_package_due_to_dimensions(self):
        """
        Checks third tier when dimensions exceed medium range.
        """
        self.assertEqual(calculate_shipping_cost(3, 31, 20, 20), 20)

    def test_large_package_mixed_invalid_conditions(self):
        """
        Checks third tier when multiple conditions fail.
        """
        self.assertEqual(calculate_shipping_cost(0.5, 15, 15, 15), 20)
