"""
White-box unittest for get_weather_advisory function.
"""

import unittest

from white_box.class_exercises import get_weather_advisory


class TestGetWeatherAdvisory(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_high_temperature_and_humidity(self):
        """
        Checks advisory when temperature > 30 and humidity > 70.
        """
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_high_temperature_boundary_not_triggered(self):
        """
        Checks temperature at boundary (30) does not trigger high advisory.
        """
        self.assertEqual(get_weather_advisory(30, 80), "No Specific Advisory")

    def test_high_humidity_boundary_not_triggered(self):
        """
        Checks humidity at boundary (70) does not trigger high advisory.
        """
        self.assertEqual(get_weather_advisory(35, 70), "No Specific Advisory")

    def test_low_temperature(self):
        """
        Checks advisory when temperature < 0.
        """
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_low_temperature_boundary_not_triggered(self):
        """
        Checks temperature at boundary (0) does not trigger low advisory.
        """
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")

    def test_no_specific_advisory_normal_conditions(self):
        """
        Checks default advisory when no conditions are met.
        """
        self.assertEqual(get_weather_advisory(25, 60), "No Specific Advisory")
