"""
White-box unittest for check_file_size function.
"""

import unittest

from white_box.class_exercises import check_file_size


class TestCheckFileSize(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_valid_size_lower_boundary(self):
        """
        Checks lower boundary (size = 0 bytes).
        """
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_valid_size_upper_boundary(self):
        """
        Checks upper boundary (size = 1048576 bytes, 1 MB).
        """
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_valid_size_middle_value(self):
        """
        Checks a valid size within range.
        """
        self.assertEqual(check_file_size(512000), "Valid File Size")

    def test_invalid_size_negative(self):
        """
        Checks negative file size.
        """
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_invalid_size_above_upper_boundary(self):
        """
        Checks size greater than 1 MB.
        """
        self.assertEqual(check_file_size(1048577), "Invalid File Size")
