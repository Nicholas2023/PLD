#!/usr/bin/python3
"""
This module defines the Place class, which is a
subclass of BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that represents a place and inherits
    from BaseModel
    Attributes:
        city_id (str): The ID of the city that the place belongs to
        user_id (str): The ID of the user who owns the place
        name (str): The name of the place
        description (str): the description of the place
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum number of guests allowed
        price_by_night (int): The price per night for the place
        latitude (float): The latitude coordinate of the place
        longitude (float): The longitude coordinate of the olace
        amenity_ids (list): A list of IDs of amenities available
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
