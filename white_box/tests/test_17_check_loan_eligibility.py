"""
White-box unittest for check_loan_eligibility function.
"""

import unittest

from white_box.class_exercises import check_loan_eligibility


class TestCheckLoanEligibility(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_not_eligible_income_below_threshold(self):
        """
        Checks income below 30000.
        """
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_standard_loan_middle_income_high_credit(self):
        """
        Checks income between 30000 and 60000 with credit_score > 700.
        """
        self.assertEqual(check_loan_eligibility(45000, 701), "Standard Loan")

    def test_secured_loan_middle_income_low_credit(self):
        """
        Checks income between 30000 and 60000 with credit_score <= 700.
        """
        self.assertEqual(check_loan_eligibility(45000, 700), "Secured Loan")

    def test_middle_income_lower_boundary(self):
        """
        Checks income at lower boundary (30000).
        """
        self.assertEqual(check_loan_eligibility(30000, 650), "Secured Loan")

    def test_middle_income_upper_boundary(self):
        """
        Checks income at upper boundary (60000).
        """
        self.assertEqual(check_loan_eligibility(60000, 720), "Standard Loan")

    def test_premium_loan_high_income_high_credit(self):
        """
        Checks income above 60000 with credit_score > 750.
        """
        self.assertEqual(check_loan_eligibility(80000, 751), "Premium Loan")

    def test_standard_loan_high_income_low_credit(self):
        """
        Checks income above 60000 with credit_score <= 750.
        """
        self.assertEqual(check_loan_eligibility(80000, 750), "Standard Loan")
