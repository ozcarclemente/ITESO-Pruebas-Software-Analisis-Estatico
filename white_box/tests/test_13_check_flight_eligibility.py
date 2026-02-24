"""
White-box unittest for check_flight_eligibility function.
"""

import unittest

from white_box.class_exercises import check_flight_eligibility


class TestCheckFlightEligibility(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_eligible_age_lower_boundary(self):
        """
        Checks eligibility at lower age boundary (age = 18).
        """
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_eligible_age_upper_boundary(self):
        """
        Checks eligibility at upper age boundary (age = 65).
        """
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_eligible_middle_age(self):
        """
        Checks eligibility for age within valid range.
        """
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_not_eligible_below_age_and_not_frequent(self):
        """
        Checks ineligibility when age is below range and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_not_eligible_above_age_and_not_frequent(self):
        """
        Checks ineligibility when age is above range and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

    def test_eligible_frequent_flyer_underage(self):
        """
        Checks eligibility when underage but frequent flyer is True.
        """
        self.assertEqual(check_flight_eligibility(16, True), "Eligible to Book")

    def test_eligible_frequent_flyer_overage(self):
        """
        Checks eligibility when overage but frequent flyer is True.
        """
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_eligible_both_conditions_true(self):
        """
        Checks eligibility when both age range and frequent flyer are True.
        """
        self.assertEqual(check_flight_eligibility(40, True), "Eligible to Book")
