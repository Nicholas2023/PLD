#!/usr/bin/python3
"""
This module defines the City class, which is a
subclass of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that represents a city and inherits
    from BaseModel
    Attributes:
        state_id (str): The ID of the state that the city belongs to
        name (str): The name of the city
    """
    state_id = ""
    name = ""
