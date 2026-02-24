"""
White-box unittest for grade_quiz function.
"""

import unittest

from white_box.class_exercises import grade_quiz


class TestGradeQuiz(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_pass_minimum_boundaries(self):
        """
        Checks lower boundary for Pass (7 correct, 2 incorrect).
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_pass_above_boundaries(self):
        """
        Checks Pass when correct answers are above minimum and incorrect below maximum.
        """
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_conditional_pass_lower_boundaries(self):
        """
        Checks lower boundary for Conditional Pass (5 correct, 3 incorrect).
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_conditional_pass_not_meeting_pass_condition(self):
        """
        Checks Conditional Pass when Pass condition fails but second condition holds.
        """
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_fail_due_to_low_correct_answers(self):
        """
        Checks Fail when correct answers are below 5.
        """
        self.assertEqual(grade_quiz(4, 0), "Fail")

    def test_fail_due_to_high_incorrect_answers(self):
        """
        Checks Fail when incorrect answers exceed allowed threshold.
        """
        self.assertEqual(grade_quiz(7, 4), "Fail")

    def test_fail_when_only_one_condition_met(self):
        """
        Checks Fail when correct_answers >= 5 but incorrect_answers > 3.
        """
        self.assertEqual(grade_quiz(5, 4), "Fail")
