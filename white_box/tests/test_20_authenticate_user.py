"""
White-box unittest for authenticate_user function.
"""

import unittest

from white_box.class_exercises import authenticate_user


class TestAuthenticateUser(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_admin_credentials(self):
        """
        Checks exact admin credentials.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_user_valid_minimum_boundaries(self):
        """
        Checks minimum valid lengths for regular user (username=5, password=8).
        """
        self.assertEqual(authenticate_user("user1", "password"), "User")

    def test_user_valid_above_boundaries(self):
        """
        Checks valid user credentials above minimum length requirements.
        """
        self.assertEqual(authenticate_user("username", "securepass"), "User")

    def test_invalid_short_username(self):
        """
        Checks invalid when username length < 5.
        """
        self.assertEqual(authenticate_user("usr", "password"), "Invalid")

    def test_invalid_short_password(self):
        """
        Checks invalid when password length < 8.
        """
        self.assertEqual(authenticate_user("user1", "pass"), "Invalid")

    def test_invalid_both_short(self):
        """
        Checks invalid when both username and password are too short.
        """
        self.assertEqual(authenticate_user("usr", "pass"), "Invalid")

    def test_user_not_admin_but_meets_length(self):
        """
        Checks non-admin credentials that satisfy length conditions.
        """
        self.assertEqual(authenticate_user("admin1", "admin1234"), "User")

    def test_invalid_wrong_admin_password(self):
        """
        Checks username 'admin' with incorrect password.
        """
        self.assertEqual(authenticate_user("admin", "wrongpass"), "User")
