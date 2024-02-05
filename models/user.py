#!/bin/user/python3
"""
A class to store user data
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
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
        if not any(args) and len(kwargs) > 0:
            kwargs.pop('__class__')
            created_at_str = kwargs['created_at']
            kwargs['created_at'] = datetime.fromisoformat(created_at_str)
            updated_at_str = kwargs['updated_at']
            kwargs['updated_at'] = datetime.fromisoformat(updated_at_str)
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            super().__init__()
            self.email = ''
            self.password = ''
            self.first_name = ''
            self.last_name = ''
            # storage.new(self)
 
    # def to_dict(self):
    #     return {
    #         "id": str(uuid.uuid4()),
    #         "email": User.email,
    #         "password": User.password,
    #         "first_name": User.first_name,
    #         "last_name": User.last_name
    #         }
