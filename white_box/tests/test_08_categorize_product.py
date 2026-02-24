"""
White-box unittest for categorize_product function.
"""

import unittest

from white_box.class_exercises import categorize_product


class TestCategorizeProduct(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_category_a_lower_boundary(self):
        """
        Checks lower boundary of Category A (price = 10).
        """
        self.assertEqual(categorize_product(10), "Category A")

    def test_category_a_upper_boundary(self):
        """
        Checks upper boundary of Category A (price = 50).
        """
        self.assertEqual(categorize_product(50), "Category A")

    def test_category_b_lower_boundary(self):
        """
        Checks lower boundary of Category B (price = 51).
        """
        self.assertEqual(categorize_product(51), "Category B")

    def test_category_b_upper_boundary(self):
        """
        Checks upper boundary of Category B (price = 100).
        """
        self.assertEqual(categorize_product(100), "Category B")

    def test_category_c_lower_boundary(self):
        """
        Checks lower boundary of Category C (price = 101).
        """
        self.assertEqual(categorize_product(101), "Category C")

    def test_category_c_upper_boundary(self):
        """
        Checks upper boundary of Category C (price = 200).
        """
        self.assertEqual(categorize_product(200), "Category C")

    def test_category_d_below_all_ranges(self):
        """
        Checks value below all defined ranges (price < 10).
        """
        self.assertEqual(categorize_product(5), "Category D")

    def test_category_d_above_all_ranges(self):
        """
        Checks value above all defined ranges (price > 200).
        """
        self.assertEqual(categorize_product(250), "Category D")
