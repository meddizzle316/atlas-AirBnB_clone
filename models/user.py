#!/bin/user/python3
"""
A class to store user data
"""
import email
from models.base_model import BaseModel


class User(BaseModel):
    
    def __init__(self, **kwargs):
        
        if "email" in kwargs and isinstance(kwargs["email"], str):
            self.email = kwargs["email"]
        if "password" in kwargs and isinstance(kwargs["password"], str):
            self.password = kwargs["password"]
        if "first_name" in kwargs and isinstance(kwargs["first_name"], str):
            self.first_name = kwargs["first_name"]
        if "last_name" in kwargs and isinstance(kwargs["last_name"], str):
            self.last_name = kwargs["last_name"]

        def to_dict(self):
            return {
                "id": self.id,
                "email": self.email,
                "password": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name
            }
