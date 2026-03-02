"""
Unit tests for TrafficLight class.
"""

import unittest

from white_box.class_exercises import TrafficLight


class TestWhiteBoxTrafficLight(unittest.TestCase):
    """
    Traffic Light class unit tests.
    """

    def setUp(self):
        """Initialize traffic light before each test."""
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_change_state_red_to_green(self):
        """Change state from Red to Green."""
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

    def test_change_state_green_to_yellow(self):
        """Change state from Green to Yellow."""
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

    def test_change_state_yellow_to_red(self):
        """Change state from Yellow to Red."""
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_get_current_state(self):
        """Return current state."""
        self.assertEqual(self.traffic_light.get_current_state(), "Red")
