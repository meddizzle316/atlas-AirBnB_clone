#!/bin/user/python3
"""
A class to store user data
"""
import email
from models.base_model import BaseModel


class User(BaseModel):
    
    def __init__(self):
        email = ''
        password = ''
        first_name = ''
        last_name = ''
