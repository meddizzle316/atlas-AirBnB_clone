#!/bin/user/python3
"""
A class to store user data
"""
from models.base_model import BaseModel


class User(BaseModel):
    # email, password, first_name, last_name = ''
    # email = ''
    # password = ''
    # first_name = ''
    # last_name = ''
    
    def __init__(self, **kwargs):
        email = ''
        password = ''
        first_name = ''
        last_name = ''

        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        else:
            self.email = kwargs.get('email', '')
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        else:
            self.password = kwargs.get('password', '')
        if not isinstance(first_name, str):
            raise TypeError("invalid First name")
        else:
            self.first_name = kwargs.get('first_name', '')
        if not isinstance(last_name, str):
            raise TypeError("invalid last name")
        else:
            self.last_name = kwargs.get('last_name', '')

        def to_dict(self):
            return {
                "id": self.id,
                "email": self.email,
                "password": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name
            }
