"""
Unit tests for the VendingMachine class.
"""

import unittest

from white_box.class_exercises import VendingMachine


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine class unit tests.
    """

    def setUp(self):
        """
        Initialize a new VendingMachine instance before each test.
        """
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_insert_coin_success_ready_to_dispensing(self):
        """
        Checks the vending machine accepts coins when it's ready.
        """
        output = self.vending_machine.insert_coin()
        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")

    def test_insert_coin_error_when_dispensing(self):
        """
        Checks the vending machine rejects coins when it's dispensing.
        """
        self.vending_machine.state = "Dispensing"
        output = self.vending_machine.insert_coin()
        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_select_drink_success_dispensing_to_ready(self):
        """
        Checks the vending machine accepts drink selection when it's dispensing.
        """
        self.vending_machine.state = "Dispensing"
        output = self.vending_machine.select_drink()
        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Drink Dispensed. Thank you!")

    def test_select_drink_error_when_ready(self):
        """
        Checks the vending machine rejects drink selection when it's ready.
        """
        output = self.vending_machine.select_drink()
        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Invalid operation in current state.")
