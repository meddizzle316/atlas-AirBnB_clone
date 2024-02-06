#!/usr/bin/python3
"""Module to test Review()"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_isinstance(self):
        self.assertTrue(isinstance(Review.place_id, str))
        self.assertTrue(isinstance(Review.user_id, str))
        self.assertTrue(isinstance(Review.text, str))

    def test_true_review(self):
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_equal_review(self):
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
