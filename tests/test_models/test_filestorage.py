#!/usr/bin/python3
""" Module to test User()"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        storage = FileStorage()
        basemodel = BaseModel()
        storage.save()
        self.assertTrue(os.path.isfile(f"{FileStorage.__file_path}"))

if __name__ == '__main__':
    unittest.main()
