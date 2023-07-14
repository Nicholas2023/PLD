#!/usr/bin/python3
"""
Test suite for the State class of the models.state module
"""

import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """

    def setUp(self):
        """
        Set up the test environment before each test case
        """
        self.state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        """
        Test if State is a subclass of BaseModel
        """
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attr(self):
        """
        Test if 'name' attribute is a class attribute of State
        """
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
        """
        Test the type and initial value of 'name' attribute
        """
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))
