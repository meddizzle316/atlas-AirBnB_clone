#!/bin/usr/python3
"""Module to test city()"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_isinstance(self):
        self.assertTrue(isinstance(City.name, str))
        self.assertTrue(isinstance(City.state_id, str))

    def test_true_city(self):
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "id"))

    def test_equal_city(self):
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")

if __name__ == '__main__':
    unittest.main()
