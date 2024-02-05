#!/usr/bin/python3
""" Module that creates the class City """
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that holds the information of the city for airbnb clone
    """
    from models.state import State

    state_id = State.id
    name =  ''

    def to_dict(self):
        return {
            "state_id": City.state_id,
            "name": City.name
        }
