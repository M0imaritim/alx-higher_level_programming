#!/usr/bin/python3
"""Module to test Base class"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


class TestBase(unittest.TestCase):
    """method to test base class"""
    def setUp(self):
        """method to be run before tests methods"""
        Base._Base__nb_objects = 0

    def test_instantiation_with_id(self):
        """instantiation with provided id"""
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_instantiation_without_id(self):
        """Test instantiation without provided id"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_instantiation_with_negative_id(self):
        """Test instantiation with negative id"""
        obj = Base(-10)
        self.assertEqual(obj.id, -10)

    def test_instantiation_with_zero_id(self):
        """Test instantiation with zero id"""
        obj = Base(0)
        self.assertEqual(obj.id, 0)

    def test_instantiation_with_non_integer_id(self):
        """Test instantiation with non-integer id"""
        obj = Base('abc')
        self.assertEqual(obj.id, 'abc')

    def test_multiple_instantiation(self):
        """Test multiple instantiations"""
        objs = [Base() for _ in range(5)]
        self.assertEqual([obj.id for obj in objs], [1, 2, 3, 4, 5])


class TestBase_to_json_string(unittest.TestCase):
    """module to test to json string"""

    def test_empty_list(self):
        """Test to_json_string method with an empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, '[]')

    def test_none(self):
        """Test to_json_string method with None"""
        result = Base.to_json_string(None)
        self.assertEqual(result, '[]')

    def test_single_dict(self):
        """Test to_json_string method with a single dictionary"""
        test_data = [{"key": "value"}]
        result = Base.to_json_string(test_data)
        self.assertEqual(result, '[{"key": "value"}]')

    def test_multiple_dicts(self):
        """Test to_json_string method with multiple dictionaries"""
        test_data = [{"key1": "value1"}, {"key2": "value2"}]
        result = Base.to_json_string(test_data)
        self.assertEqual(result, '[{"key1": "value1"}, {"key2": "value2"}]')


class TestBase_from_json_string(unittest.TestCase):
    """testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 99, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))


if __name__ == "__main__":
    unittest.main()
