#!/usr/bin/python
""" Module that for the class of State"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class that holds the information of State for Airbnb console"""
    name = ''
    id = ''

    def to_dict(self):
        return {
            "id": id,
            "name": State.name
        }
