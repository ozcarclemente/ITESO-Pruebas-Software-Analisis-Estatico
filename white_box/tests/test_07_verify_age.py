"""
White-box unittest for verify_age function.
"""

import unittest

from white_box.class_exercises import verify_age


class TestVerifyAge(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_age_eligible_lower_boundary(self):
        """
        Age at the lower eligibility boundary should be eligible.
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_age_eligible_upper_boundary(self):
        """
        Age at the upper eligibility boundary should be eligible.
        """
        self.assertEqual(verify_age(65), "Eligible")

    def test_age_too_young(self):
        """
        Age just below eligibility should be not eligible.
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_too_old(self):
        """
        Age just above eligibility should be not eligible.
        """
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_age_negative(self):
        """
        Negative ages are invalid and should be not eligible.
        """
        self.assertEqual(verify_age(-1), "Not Eligible")
