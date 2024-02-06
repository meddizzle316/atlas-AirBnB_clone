#!/usr/bin/python3
""" Module to test console.py """
from os import name
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_true(self):
        self.assertTrue(hasattr(State(), name))

    def test_equal(self):
        self.assertEqual(State(), " ")
        
