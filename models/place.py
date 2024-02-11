#!/usr/bin/python3
"""Module that stores location data"""
from models.base_model import BaseModel
from models.city import City
from models.user import User

class Place(BaseModel):
    """
    Class that stores location information
    """
    city_id = '' #will be City.id
    user_id = '' #will be User.id
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] #will be list of Amenity.id

    def __init__(self, *args, **kwargs):
        """
        Initialization of the State class
        """
        super().__init__(*args, **kwargs)

