#!/usr/bin/python3
"""a module for the class FileStorage"""
import json
import os


class FileStorage():
    """class that deals with file storage"""
    __file_path = 'file.json'
    __objects = {} #empty dictionary to hold everything by <class name>.id ex Basemodel.12121212

    def all(self):
        """returns all objects stored in FileStorage"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """converts __objects to json string in __file_path"""
        dict_of_dict = {}
        for key, value in self.__objects.items():
            dict_of_dict[key] = value.to_dict() 
        with open(self.__file_path, "w") as file:
            json.dump(dict_of_dict, file, indent=4)


    def classes(self):
        """returns a dictionary of valid classes"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes                
        
    def reload(self):
        """converts json strings in __file_path to __objects"""
        if not os.path.isfile(f"{FileStorage.__file_path}"):
            pass
        else:
            with open(f"{FileStorage.__file_path}", 'r') as file:
                python_dict = json.loads(file.read()) 
                for id, dictionary in python_dict.items():
                    class_name = dictionary['__class__']
                    FileStorage.__objects[id] = self.classes()[class_name](**dictionary)
