#!/usr/bin/python3
"""
base class for all other classes
in AirBnB project
"""
from datetime import datetime
import uuid
from dataclasses import dataclass, asdict

@dataclass
class BaseModel:
    """
    basemodel class -- original class
    has common methods and attributes
    """

    def __init__(self):
        """init function for Basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str representation of Basemodel"""
        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"

    def save(self):
        """updates updated_at attribute"""
        self.updated_at = datetime.now()

    # def to_dict(self):
    #     """converts object to dict to prepare for json conversion"""
    #     new_dict = vars(self)
    #     new_dict['__class__'] = self.__class__.__name__
    #     new_dict['created_at'] = self.created_at.isoformat()
    #     new_dict['updated_at'] = self.updated_at.isoformat()
    #     return new_dict
    

    def to_dict(self):
        """experimental attempt at not using vars"""
        d = {}
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        for a in vars(self):
            d.update({a: getattr(self, a)})
        d['__class__'] = self.__class__.__name__
        return d
