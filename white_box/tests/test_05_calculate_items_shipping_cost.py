"""
White-box unittest for calculate_items_shipping_cost function.
"""

import unittest

from white_box.class_exercises import calculate_items_shipping_cost


class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_calculate_items_shipping_cost_standard_light(self):
        """
        Checks standard shipping cost for a light package (total weight <= 5).
        """
        items = [{"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_medium(self):
        """
        Checks standard shipping cost for a medium package (5 < total weight <= 10).
        """
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_heavy(self):
        """
        Checks standard shipping cost for a heavy package (total weight > 10).
        """
        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_light(self):
        """
        Checks express shipping cost for a light package (total weight <= 5).
        """
        items = [{"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_medium(self):
        """
        Checks express shipping cost for a medium package (5 < total weight <= 10).
        """
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_heavy(self):
        """
        Checks express shipping cost for a heavy package (total weight > 10).
        """
        items = [{"weight": 20}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_empty_items(self):
        """
        Checks behavior when the items list is empty (total weight == 0).
        For standard shipping this should return the light-rate of 10.
        """
        items = []
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_invalid_method(self):
        """
        Verifies that an invalid shipping method raises a ValueError.
        """
        items = [{"weight": 1}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "overnight")
