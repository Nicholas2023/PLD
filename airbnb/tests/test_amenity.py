#!/usr/bin/python3
"""
This module contains a test suite for the Amenity
class of the models.amenity module.
"""

import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Test fixture setup method.
        This method is called before each test case
        to set up the environment.
        """
        self.amenity = Amenity()

    def test_amenity_is_a_subclass_of_basemodel(self):
        """
        Test case to verify that Amenity is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr_is_a_class_attr(self):
        """
        Test case to verify that 'name' is a class attribute of Amenity.
        """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        """
        Test case to verify the properties of the 'name' class
        attribute of Amenity.
        """
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))
