#!/usr/bin/python3
"""
This module defines the Review class, which is a
subclass of BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that represents a review and inherits
    from BaseModel
    Attributes:
        place_id (str): The ID of the place that the review belongs to
        user_id (str): The ID of the user who wrote the review
        text (str): the content of the review
    """
    place_id = ""
    user_id = ""
    text = ""
