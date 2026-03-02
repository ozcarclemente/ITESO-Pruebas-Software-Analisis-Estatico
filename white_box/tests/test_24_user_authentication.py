"""
Unit tests for UserAuthentication class.
"""

import unittest

from white_box.class_exercises import UserAuthentication


class TestWhiteBoxUserAuthentication(unittest.TestCase):
    """
    UserAuthentication class unit tests.
    """

    def setUp(self):
        """Initialize authentication system."""
        self.auth = UserAuthentication()
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_success(self):
        """Login from Logged Out state."""
        output = self.auth.login()
        self.assertEqual(self.auth.state, "Logged In")
        self.assertEqual(output, "Login successful")

    def test_login_invalid_when_logged_in(self):
        """Login when already Logged In (invalid)."""
        self.auth.state = "Logged In"
        output = self.auth.login()
        self.assertEqual(self.auth.state, "Logged In")
        self.assertEqual(output, "Invalid operation in current state")

    def test_logout_success(self):
        """Logout from Logged In state."""
        self.auth.state = "Logged In"
        output = self.auth.logout()
        self.assertEqual(self.auth.state, "Logged Out")
        self.assertEqual(output, "Logout successful")

    def test_logout_invalid_when_logged_out(self):
        """Logout when already Logged Out (invalid)."""
        output = self.auth.logout()
        self.assertEqual(self.auth.state, "Logged Out")
        self.assertEqual(output, "Invalid operation in current state")
