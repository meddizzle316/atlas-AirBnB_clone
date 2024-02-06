#!/usr/bin/python3
""" Module to test state.py """
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_true(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_equal(self):
        state = State()
        self.assertEqual(State.name, "")

if __name__ == '__main__':
    unittest.main()
