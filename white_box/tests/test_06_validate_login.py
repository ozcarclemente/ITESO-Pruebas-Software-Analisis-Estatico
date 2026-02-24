"""
White-box unittest for validate_login function.
"""

import unittest

from white_box.class_exercises import validate_login


class TestValidateLogin(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_login_success_min_boundary(self):
        """
        Valid username/password at minimum allowed lengths should succeed.
        """
        username = "user1"  # length 5
        password = "Passw0rd"  # length 8
        self.assertEqual(validate_login(username, password), "Login Successful")

    def test_login_success_max_boundary(self):
        """
        Valid username/password at maximum allowed lengths should succeed.
        """
        username = "u" * 20  # length 20
        password = "P" * 15  # length 15
        self.assertEqual(validate_login(username, password), "Login Successful")

    def test_username_too_short(self):
        """
        Username shorter than minimum length should fail login.
        """
        username = "usr"  # length 3
        password = "Passw0rd"
        self.assertEqual(validate_login(username, password), "Login Failed")

    def test_username_too_long(self):
        """
        Username longer than maximum length should fail login.
        """
        username = "u" * 21  # length 21
        password = "Passw0rd"
        self.assertEqual(validate_login(username, password), "Login Failed")

    def test_password_too_short(self):
        """
        Password shorter than minimum length should fail login.
        """
        username = "validuser"
        password = "Short7"  # length 6
        self.assertEqual(validate_login(username, password), "Login Failed")

    def test_password_too_long(self):
        """
        Password longer than maximum length should fail login.
        """
        username = "validuser"
        password = "P" * 16  # length 16
        self.assertEqual(validate_login(username, password), "Login Failed")

    def test_both_invalid(self):
        """
        Both username and password invalid should fail login.
        """
        username = "u" * 2
        password = "p" * 2
        self.assertEqual(validate_login(username, password), "Login Failed")
