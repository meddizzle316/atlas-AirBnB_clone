#!/usr/bin/python3
"""Module that stores amenity information"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Class that Stores amenity data """

    name = ''
    def __init__(self, *args, **kwargs):
        """
        Initialization of the State class
        """
        super().__init__(*args, **kwargs)
    
