#!/bin/user/python3
"""
A class to store user data
"""
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(self, id)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
