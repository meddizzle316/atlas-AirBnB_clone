#!/bin/usr/python3
"""Module to test city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_true_city(self):
        city = City()
        self.assertTrue(hasattr(city, "name"))

    def test_equal_city(self):
        self.assertEqual(City.name, "")

if __name__ == '__main__':
    unittest.main()
