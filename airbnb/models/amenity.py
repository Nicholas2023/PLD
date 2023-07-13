#!/usr/bin/python3
"""
This module defines the Amenity class, which is
a subclass of BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that represents an amenity and inherits
    from Basemodel
    Attributes:
        name (str): The name of the amenity
    """
    name = ""
