#!/usr/bin/python3
"""
Test suite for the Review class in models.review module.
This module contains a test suite for the Review class,
which is responsible for representing and handling review data.
The Review class is a subclass of the BaseModel class.
"""

import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    This class provides test cases to verify the
    behavior and functionality of the Review class.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        This method is executed before each individual test
        case to set up the necessary objects and variables.
        In this case, it initializes a new instance of the Review
        class and a list of attribute names to test against.
        """
        self.review = Review()
        self.attr_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_review_is_a_subclass_of_basemodel(self):
        """
        Test if Review is a subclass of BaseModel.
        This test case verifies that the Review class
        inherits from the BaseModel class.
        """
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attrs_are_class_attrs(self):
        """
        Test if attributes are class attributes.
        This test case checks if the attributes defined in
        the Review class are class attributes.
        """
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_class_attrs(self):
        """
        Test class attributes.
        This test case ensures that the class attributes in the
        Review class are of the correct type and initial value.
        """
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))
