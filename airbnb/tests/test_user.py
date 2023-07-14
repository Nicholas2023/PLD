#!/usr/bin/python3
"""
Test suite for the User class in models.user.

This module contains test cases to verify the behavior of the User class
defined in the models.user module. It utilizes the unittest framework
to define and run the tests.

Example:
    Run this module as a standalone script to execute all the tests:

        $ python test_user.py

    Alternatively, you can use a test runner, such as `unittest` command:

        $ python -m unittest test_user

Attributes:
    None.

Classes:
    TestUser: A TestCase class containing test cases for the User class.

Functions:
    None.
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases against the User class.

    This class contains test cases to validate the behavior of the User class.
    It extends the TestCase class from the unittest module and defines various
    test methods to cover different aspects of the User class.

    Attributes:
        None.
    """

    def test_attrs_are_class_attrs(self):
        """
        Test if first_name and last_name are class attributes.

        This method verifies that the first_name and last_name attributes of
        the User class are defined as class attributes.

        Args:
            None.

        Returns:
            None.

        Raises:
            AssertionError: If either first_name or last_name is not a class
                attribute of the User class.
        """
        u = User()
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
        """
        Test the type and initial values of first_name and last_name.

        This method checks that the first_name and last_name attributes of a
        User instance are of the correct type (str) and have the expected
        initial values (empty strings).

        Args:
            None.

        Returns:
            None.

        Raises:
            AssertionError: If either first_name or last_name is not of type
                str, or if their initial values are not empty strings.
        """
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def test_user_is_a_subclass_of_basemodel(self):
        """
        Test if User is a subclass of BaseModel.

        This method verifies that the User class is a subclass of the BaseModel
        class.

        Args:
            None.

        Returns:
            None.

        Raises:
            AssertionError: If User is not a subclass of BaseModel.
        """
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
