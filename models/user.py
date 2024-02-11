#!/bin/user/python3
"""
A class to store user data
"""
from models.base_model import BaseModel
import uuid
from models import storage

class User(BaseModel):
    """
    class that stores User data
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(*args, **kwargs)
