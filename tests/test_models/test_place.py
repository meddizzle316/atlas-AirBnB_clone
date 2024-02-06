#!/usr/bin/python3
"""Module to test Place()"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_instance(self):
        self.assertTrue(isinstance(Place.city_id, str))
        self.assertTrue(isinstance(Place.user_id, str))
        self.assertTrue(isinstance(Place.name, str))
        self.assertTrue(isinstance(Place.description, str))
        self.assertTrue(isinstance(Place.number_rooms, int))
        self.assertTrue(isinstance(Place.number_bathrooms, int))
        self.assertTrue(isinstance(Place.max_guest, int))
        self.assertTrue(isinstance(Place.price_by_night, int))
        self.assertTrue(isinstance(Place.latitude, float))
        self.assertTrue(isinstance(Place.longitude, float))
        self.assertTrue(isinstance(Place.amenity_ids, list))

    def test_true_place(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_equal_place(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.price_by_night, 0.0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
