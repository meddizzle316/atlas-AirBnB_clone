#!/usr/bin/python3
""" Module to test console.py """
import unittest
from models import base_model, city, state, user, amenity, place, review
from models.engine import file_storage


class TestState(unittest.TestCase):
    
