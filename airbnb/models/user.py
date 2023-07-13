#!/usr/bin/python3
"""
A module that contains User information
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    Public class attributes:
        email (str): Initialized as an empty string
        password (str): Initialized as an empty string
        first_name (str): Initialized as an empty string
        last_name (str): Initialized as an empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
