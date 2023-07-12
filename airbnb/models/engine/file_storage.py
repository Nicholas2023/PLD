#!/usr/bin/python3
"""
A module that implemets a FileStorage class
"""

import json

from models.base_model import BaseModel


class FileStorage:
    """
    Class that serializes instances to a JSON file and deserializes
    JSON file to instances
    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store objects by <class name>.id
    Methods:
        all (self): Returns the dictionary of all stored objects.
        new(self, obj): Sets a new object in __objects with the key
        <obj class name>.id.
        save(self): Serializes __objects to the JSON file.
        reload(self): Deserializes the JSON file to __objects (if it exists)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all stored objects.
        Returns:
            dict: Dictionary of objects by <class name>.id
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in __objects with the key <obj class name>.id
        Args:
            obj: The object to be stored
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            obj_dict = {}
            for key, obj in self.__objects.items():
                obj_dict[key] = obj.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if it exists)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    cls = BaseModel if cls_name == "BaseModel" else None
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            return
