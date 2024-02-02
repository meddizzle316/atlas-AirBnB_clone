#!/usr/bin/python3
"""a module for the class FileStorage"""
from models.base_model import BaseModel
import json
import os

class FileStorage(BaseModel):
    """class that deals with file storage"""
    __file_path = 'file.json'
    __objects = {} #empty dictionary to hold everything by <class name>.id ex Basemodel.12121212

    def all(self):
        """returns all objects stored in FileStorage"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """converts __objects to json string in __file_path"""
        json.dump(FileStorage.__objects, FileStorage.__file_path)

    def reload(self):
        """converts json strings in __file_path to __objects"""
        if not os.path.isfile(f"{FileStorage.__file_path}"):
            pass
        else:
            with open(f"{FileStorage.__file_path}", 'r') as file:
                python_dict = json.loads(file.read()) #I think the return python object is a dict, not sure
                for key, value in python_dict.items():
                    setattr(FileStorage.__objects, key, value)
