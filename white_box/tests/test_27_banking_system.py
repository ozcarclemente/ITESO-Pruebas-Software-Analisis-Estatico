"""
Banking system unit testing examples.
"""

import unittest
from unittest.mock import patch

from white_box.class_exercises import BankAccount, BankingSystem


class TestBankAccount(unittest.TestCase):
    """
    BankAccount unittest class.
    """

    def setUp(self):
        """
        Creates the account properties.
        """
        self.account_number = "ACC123"
        self.balance = 500

    def test_bank_account_init(self):
        """
        Checks the bank account properties.
        """
        account = BankAccount(self.account_number, self.balance)
        self.assertEqual(account.account_number, self.account_number)
        self.assertEqual(account.balance, self.balance)

    @patch("builtins.print")
    def test_view_account(self, mock_print):
        """
        Checks the account display function.
        """
        account = BankAccount(self.account_number, self.balance)
        account.view_account()

        printed_msg = (
            f"The account {self.account_number} has a balance of {self.balance}"
        )

        mock_print.assert_called_once_with(printed_msg)


class TestBankingSystem(unittest.TestCase):
    """
    BankingSystem unittest class.
    """

    username = "user123"
    password = "pass123"
    username2 = "user456"

    def test_banking_system_init(self):
        """
        Checks the banking system initial properties.
        """

        banking_system = BankingSystem()
        self.assertEqual(banking_system.users, {self.username: self.password})
        self.assertEqual(banking_system.logged_in_users, set())

    def test_authenticate_success(self):
        """
        Checks successful authentication.
        """
        banking_system = BankingSystem()
        with patch("builtins.print") as mock_print:
            result = banking_system.authenticate(self.username, self.password)
            self.assertTrue(result)
            self.assertIn(self.username, banking_system.logged_in_users)

            printed_msg = f"User {self.username} authenticated successfully."

            mock_print.assert_called_once_with(printed_msg)

    @patch("builtins.print")
    def test_authenticate_already_logged_in(self, mock_print):
        """
        Checks authentication when user is already logged in.
        """
        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        result = banking_system.authenticate(self.username, self.password)

        self.assertFalse(result)

        printed_msg = "User already logged in."

        mock_print.assert_called_once_with(printed_msg)

    def test_authenticate_failed(self):
        """
        Checks failed authentication.
        """
        banking_system = BankingSystem()

        wrong_password = "wrongpass"

        with patch("builtins.print") as mock_print:
            result = banking_system.authenticate(self.username, wrong_password)
            self.assertFalse(result)
            self.assertNotIn(self.username, banking_system.logged_in_users)
            printed_msg = "Authentication failed."
            mock_print.assert_called_once_with(printed_msg)

    def test_transfer_money_sender_not_authenticated(self):
        """
        Checks transfer fails when sender is not authenticated.
        """
        banking_system = BankingSystem()

        amount = 100
        transaction_type = "regular"

        with patch("builtins.print") as mock_print:
            result = banking_system.transfer_money(
                self.username, self.username2, amount, transaction_type
            )
            self.assertFalse(result)
            printed_msg = "Sender not authenticated."
            mock_print.assert_called_once_with(printed_msg)

    @patch("builtins.print")
    def test_transfer_money_regular_success(self, mock_print):
        """
        Checks successful regular transfer.
        """

        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        amount = 100
        transaction_type = "regular"

        result = banking_system.transfer_money(
            self.username, self.username2, amount, transaction_type
        )
        self.assertTrue(result)
        printed_msg = (
            f"Money transfer of ${amount} ({transaction_type} transfer) "
            f"from {self.username} to {self.username2} processed successfully."
        )
        mock_print.assert_called_once_with(printed_msg)

    @patch("builtins.print")
    def test_transfer_money_express_success(self, mock_print):
        """
        Checks successful express transfer.
        """
        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        amount = 100
        transaction_type = "express"

        result = banking_system.transfer_money(
            self.username, self.username2, amount, transaction_type
        )
        self.assertTrue(result)
        printed_msg = (
            f"Money transfer of ${amount} ({transaction_type} transfer) "
            f"from {self.username} to {self.username2} processed successfully."
        )
        mock_print.assert_called_once_with(printed_msg)

    @patch("builtins.print")
    def test_transfer_money_scheduled_success(self, mock_print):
        """
        Checks successful scheduled transfer.
        """
        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        amount = 100
        transaction_type = "scheduled"

        result = banking_system.transfer_money(
            self.username, self.username2, amount, transaction_type
        )
        self.assertTrue(result)
        printed_msg = (
            f"Money transfer of ${amount} ({transaction_type} transfer) "
            f"from {self.username} to {self.username2} processed successfully."
        )
        mock_print.assert_called_once_with(printed_msg)

    @patch("builtins.print")
    def test_transfer_money_invalid_transaction_type(self, mock_print):
        """
        Checks transfer fails with invalid transaction type.
        """
        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        amount = 100
        transaction_type = "invalid"

        result = banking_system.transfer_money(
            self.username, self.username2, amount, transaction_type
        )
        self.assertFalse(result)
        printed_msg = "Invalid transaction type."
        mock_print.assert_called_once_with(printed_msg)

    # Tests for insufficient funds scenarios
    insuficient_msg = "Insufficient funds."

    @patch("builtins.print")
    def test_transfer_money_regular_insufficient_funds(self, mock_print):
        """
        Checks regular transfer fails due to insufficient funds.
        """
        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        amount = 5000
        transaction_type = "regular"

        result = banking_system.transfer_money(
            self.username, self.username2, amount, transaction_type
        )
        self.assertFalse(result)
        mock_print.assert_called_once_with(self.insuficient_msg)

    @patch("builtins.print")
    def test_transfer_money_express_insufficient_funds(self, mock_print):
        """
        Checks express transfer fails due to insufficient funds.
        """
        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        amount = 5000
        transaction_type = "express"

        result = banking_system.transfer_money(
            self.username, self.username2, amount, transaction_type
        )
        self.assertFalse(result)
        mock_print.assert_called_once_with(self.insuficient_msg)

    @patch("builtins.print")
    def test_transfer_money_scheduled_insufficient_funds(self, mock_print):
        """
        Checks scheduled transfer fails due to insufficient funds.
        """
        banking_system = BankingSystem()
        banking_system.authenticate(self.username, self.password)
        mock_print.reset_mock()

        amount = 5000
        transaction_type = "scheduled"

        result = banking_system.transfer_money(
            self.username, self.username2, amount, transaction_type
        )
        self.assertFalse(result)
        mock_print.assert_called_once_with(self.insuficient_msg)
