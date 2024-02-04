#!/bin/user/python3
"""
A class to store user data
"""
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
