"""
White-box unittest for celsius_to_fahrenheit function.
"""

import unittest

from white_box.class_exercises import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_lower_boundary_valid(self):
        """
        Checks lower valid boundary (celsius = -100).
        """
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)

    def test_upper_boundary_valid(self):
        """
        Checks upper valid boundary (celsius = 100).
        """
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_zero_conversion(self):
        """
        Checks conversion of 0°C.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_positive_middle_value(self):
        """
        Checks conversion of a positive value within range.
        """
        self.assertEqual(celsius_to_fahrenheit(25), 77.0)

    def test_negative_middle_value(self):
        """
        Checks conversion of a negative value within range.
        """
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_below_lower_boundary_invalid(self):
        """
        Checks value below valid range (celsius < -100).
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_above_upper_boundary_invalid(self):
        """
        Checks value above valid range (celsius > 100).
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")
