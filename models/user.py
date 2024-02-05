#!/bin/user/python3
"""
A class to store user data
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class that stores User data
    """
    
    def __init__(self):
        """
        Initialization
        """
        email = ''
        password = ''
        first_name = ''
        last_name = ''

        def to_dict(self):
            return {
                "id": id,
                "email": email,
                "password": password,
                "first_name": first_name,
                "last_name": last_name
            }
