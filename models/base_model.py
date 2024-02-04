#!/usr/bin/python3
"""
base class for all other classes
in AirBnB project
"""
from datetime import datetime
import uuid
from models import storage


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
            created_at_str = kwargs['created_at']
            kwargs['created_at'] = datetime.fromisoformat(created_at_str)
            updated_at_str = kwargs['updated_at']
            kwargs['updated_at'] = datetime.fromisoformat(updated_at_str)
            for k, v in kwargs.items():
                setattr(self, k, v)

        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.name = 'default'
            self.my_number = 2
            storage.new(self) ## hopefully this is what  they wanted


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
        storage.save()
        # self.updated_at = datetime.now()

    def to_dict(self):
        """
        yet another attempt to 
        convert object to dictionary
        """
        d = {}
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['created_at'] = self.created_at.isoformat()
        attributes = ['my_number', 'name', '__class__', 'updated_at', 'id', 'created_at']
        for a in attributes:
            d.update({a: getattr(self, a)})
        d['__class__'] = self.__class__.__name__
        return d
