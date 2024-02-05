#!/bin/user/python3
"""
A class to store user data
"""
from models.base_model import BaseModel
import uuid

class User(BaseModel):
    """
    class that stores User data
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
    def __init__(self):
        """
        Initialization
        """
        super().__init__()

    def to_dict(self):
        return {
            "id": str(uuid.uuid4()),
            "email": User.email,
            "password": User.password,
            "first_name": User.first_name,
            "last_name": User.last_name
            }
