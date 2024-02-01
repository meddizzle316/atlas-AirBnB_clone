#!/usr/bin/python3
"""
base class for all other classes
in AirBnB project
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    basemodel class -- original class
    has common methods and attributes
    """

    def __init__(self, *args, **kwargs):
        """
        init function for Basemodel adds 
        attributes
        """
        if not any(args) and len(kwargs) > 0:
            kwargs.pop('__class__')
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """
        str representation of Basemodel
        prints name, id and dict
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})"
       
    def save(self):
        """
        updates updated_at attribute
        uses datetime.now() to set time
        """
        self.updated_at = datetime.now()

    # def to_dict(self):
    #     """
    #     experimental attempt at not using vars
    #     """
    #     self.save()
    #     d = {}
    #     for a in vars(self):
    #         d.update({a: getattr(self, a)})
    #     d['__class__'] = self.__class__.__name__
    #     d['created_at'] = self.created_at.isoformat()
    #     d['updated_at'] = self.updated_at.isoformat()
    #     return d

    def to_dict(self):
        """
        yet another attempt to 
        convert object to dictionary
        """
        self.save()
        d = {}
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['created_at'] = self.created_at.isoformat()
        attributes = ['my_number', 'name', '__class__', 'updated_at', 'id', 'created_at']
        for a in attributes:
            d.update({a: getattr(self, a)})
        d['__class__'] = self.__class__.__name__
        return d
