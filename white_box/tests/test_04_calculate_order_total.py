"""
White-box unittest for calculate_order_total function.
"""

import unittest

from white_box.class_exercises import calculate_order_total


class TestCalculateOrderTotal(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_calculate_order_total_no_items(self):
        """
        Checks if the total price is 0 when there are no items in the order.
        """
        self.assertEqual(calculate_order_total([]), 0)

    def test_calculate_order_total_single_item(self):
        """
        Checks if the total price is correct when there is a single item in the order.
        """
        items = [{"price": 10, "quantity": 1}]
        self.assertEqual(calculate_order_total(items), 10)

    def test_calculate_order_total_single_item_with_5_percent_discount(self):
        """
        Checks if the total price is correct
        when there is a single item in the order with 5% discount.
        """
        items = [{"price": 10, "quantity": 8}]
        self.assertEqual(calculate_order_total(items), 80 * 0.95)

    def test_calculate_order_total_single_item_with_10_percent_discount(self):
        """
        Checks if the total price is correct
        when there is a single item in the order with 10% discount.
        """
        items = [{"price": 10, "quantity": 15}]
        self.assertEqual(calculate_order_total(items), 150 * 0.9)

    def test_calculate_order_total_multiple_items(self):
        """
        Checks if the total price is correct
        when there are multiple items in the order with different discounts.
        """
        items = [
            {"price": 10, "quantity": 1},
            {"price": 20, "quantity": 8},
            {"price": 30, "quantity": 16},
        ]
        self.assertEqual(calculate_order_total(items), 10 + 160 * 0.95 + 480 * 0.9)

    def test_calculate_order_total_boundary_quantities(self):
        """
        Checks boundary quantities that exercise all branches (5, 6, 10).
        """
        items = [
            {"price": 10, "quantity": 5},  # no discount
            {"price": 20, "quantity": 6},  # 5% discount
            {"price": 5, "quantity": 10},  # 5% discount (boundary)
        ]
        expected = 5 * 10 + 0.95 * 6 * 20 + 0.95 * 10 * 5
        self.assertAlmostEqual(calculate_order_total(items), expected, places=5)

    def test_calculate_order_total_zero_quantity(self):
        """
        Zero quantity should result in zero total
        for that item (current implementation uses else branch).
        """
        items = [{"price": 10, "quantity": 0}]
        self.assertEqual(calculate_order_total(items), 0)

    def test_calculate_order_total_negative_price(self):
        """
        Negative prices propagate through the calculation (white-box edge case).
        """
        items = [{"price": -10, "quantity": 2}]
        self.assertEqual(calculate_order_total(items), -20)

    def test_calculate_order_total_large_quantity(self):
        """
        Large quantities exercise the else branch (10% discount).
        """
        items = [{"price": 1, "quantity": 1000}]
        self.assertEqual(calculate_order_total(items), 0.9 * 1000 * 1)
