#!/usr/bin/python3
""" Module that creates the class City """
from models.base_model import BaseModel
from datetime import datetime
from models.state import State

class City(BaseModel):
    """
    Class that holds the information of the city for airbnb clone
    """
    # from models.state import State

    state_id = State.id
    name =  ''

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
            self.state_id = '' #will be State.id
            self.name = ''
