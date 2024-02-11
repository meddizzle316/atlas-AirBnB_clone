#!/usr/bin/python3
"""Module that stores review data"""
from models.base_model import BaseModel
from datetime import datetime

class Review(BaseModel):
    """
    Class that stores review data
    """
    place_id = ''
    user_id = ''
    text = ''
    
    def __init__(self, *args, **kwargs):
        """
        Initialization of the State class
        """
        super().__init__(*args, **kwargs)
