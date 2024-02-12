#!/usr/bin/python3
"""Module contains test cases for class rectangle"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """class containing rectangle tests"""

    def test_constructor(self):
        """Test constructor with valid arguments"""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

        """Test constructor with default arguments"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 2)

    def test_width_setter(self):
        """Test width setter with valid value"""
        rect = Rectangle(5, 10)
        rect.width = 7
        self.assertEqual(rect.width, 7)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height_setter(self):
        """Test height setter with valid value"""
        rect = Rectangle(5, 10)
        rect.height = 15
        self.assertEqual(rect.height, 15)

        with self.assertRaises(ValueError):
            rect.height = -10

    def test_x_setter(self):
        """Test x setter with valid value"""
        rect = Rectangle(5, 10)
        rect.x = 3
        self.assertEqual(rect.x, 3)

        with self.assertRaises(ValueError):
            rect.x = -2

    def test_y_setter(self):
        """Test y setter with valid value"""
        rect = Rectangle(5, 10)
        rect.y = 4
        self.assertEqual(rect.y, 4)

        with self.assertRaises(ValueError):
            rect.y = -3

    def test_area(self):
        """test area method"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_str(self):
        """Test str method"""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_update(self):
        """Test update method with args"""
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(7, 8, 9, 4, 5)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

        rect.update(width=12, height=15, x=6, y=7)
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 7)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.to_dictionary(), {'id': 1, 'width': 5,
                                                'height': 10, 'x': 2, 'y': 3})


if __name__ == '__main__':
    unittest.main()
