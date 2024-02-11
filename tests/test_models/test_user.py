#!/usr/bin/python3
""" Module to test User()"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))


if __name__ == '__main__':
    unittest.main()
