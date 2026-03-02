"""
Unit tests for ElevatorSystem class.
"""

import unittest

from white_box.class_exercises import ElevatorSystem


class TestWhiteBoxElevatorSystem(unittest.TestCase):
    """
    ElevatorSystem class unit tests.
    """

    def setUp(self):
        """Initialize elevator system."""
        self.elevator = ElevatorSystem()
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_success(self):
        """Move up from Idle state."""
        output = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(output, "Elevator moving up")

    def test_move_up_invalid_when_not_idle(self):
        """Move up when not Idle (invalid)."""
        self.elevator.state = "Moving Down"
        output = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(output, "Invalid operation in current state")

    def test_move_down_success(self):
        """Move down from Idle state."""
        output = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(output, "Elevator moving down")

    def test_move_down_invalid_when_not_idle(self):
        """Move down when not Idle (invalid)."""
        self.elevator.state = "Moving Up"
        output = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(output, "Invalid operation in current state")

    def test_stop_from_moving_up(self):
        """Stop elevator when Moving Up."""
        self.elevator.state = "Moving Up"
        output = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_stop_from_moving_down(self):
        """Stop elevator when Moving Down."""
        self.elevator.state = "Moving Down"
        output = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_stop_invalid_when_idle(self):
        """Stop when already Idle (invalid)."""
        output = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Invalid operation in current state")
