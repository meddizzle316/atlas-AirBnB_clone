#!/usr/bin/python3
""" Module that creates the class City """
from models.base_model import BaseModel
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
        super().__init__(*args, **kwargs)
