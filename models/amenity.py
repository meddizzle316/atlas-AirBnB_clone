#!/usr/bin/python3
"""Module that stores amenity information"""
from models.base_model import BaseModel
from datetime import datetime

class Amenity(BaseModel):
    """ Class that Stores amenity data """

    name = ''
    def __init__(self, *args, **kwargs):
        """
        Initialization of the State class
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
            self.name = ''
    
