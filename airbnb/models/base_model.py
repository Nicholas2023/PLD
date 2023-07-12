#!/usr/bin/python3
"""
A module that implements the BaseModel for AirBnB project
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for other classes with common attributes and methods
    Attributes:
        id (str): Unique identifier for the instances
        created_at (datetime): The datetime when the instance was created
        updated_at (datetime): The datetime when the instance was last updated
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel
        Attributes:
            id (str): Set to a unique identifier generated
            using `uuid.uuid4()`
            created_at (datetime): Set to current datetime
            updated_at (datetime): Set to current datetime
        Args:
            *args: Variable length arg list
            **kwargs: Arbitrary keyword arg containing attributes names
            and their values
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance
        Returns:
            str: The string representation of the instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime
        This method is called to indicate that the instance has
        been updated
        It updates the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance
        The dictionary contains all the instance attributes and their values
        It includes the class name, created_at, and updated_at attributes
        Returns:
            dict: The dictionary representation of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
