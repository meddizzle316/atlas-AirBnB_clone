#!/usr/bin/python3
"""Module to test Amenity()"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_isinstance(self):
        self.assertTrue(isinstance(Amenity.name, str))

    def test_true_amenity(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_equal_amenity(self):
        amenity = Amenity()
        self.assertEqual(Amenity.name, "")
