#!/usr/bin/python3
""" Module to test State()"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_isinstance(self):
        self.assertTrue(type(State.name), str)

    def test_true_state(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_equal_state(self):
        state = State()
        self.assertEqual(State.name, "")

if __name__ == '__main__':
    unittest.main()
