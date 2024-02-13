#!/usr/bin/python3
""" Module to test User()"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_email(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_user_password(self):
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_user_first_name(self):
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        
    def test_user_last_name(self):
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
