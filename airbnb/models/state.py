#!/usr/bin/python3
"""
This module defines the State class, which is
a subclass of BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that represents a state and inherits
    from BaseModel

    Attributes:
        name (str): The name of the state.
    """
    name = ""
