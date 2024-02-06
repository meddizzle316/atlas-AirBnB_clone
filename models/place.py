#!/usr/bin/python3
"""Module that stores location data"""
from models.base_model import BaseModel
from datetime import datetime
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
            self.city_id = '' #will be City.id
            self.user_id = '' #will be User.id
            self.name = ''
            self.description = ''
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = [] #will be list of Amenity.id
