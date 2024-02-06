#!/usr/bin/python
""" Module that for the class of State"""
from models.base_model import BaseModel
from datetime import datetime

class State(BaseModel):
    """ Class that holds the information of State for Airbnb console"""
    name = ''
    id = ''

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
