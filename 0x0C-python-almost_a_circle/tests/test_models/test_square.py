#!/usr/bin/python3
""" Module for test Square class """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Unittests for the Square class."""

    def test_constructor(self):
        """Test constructor with valid arguments"""
        sqr = Square(5, 2, 3, 1)
        self.assertEqual(sqr.size, 5)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 3)
        self.assertEqual(sqr.id, 1)

        sqr = Square(5)
        self.assertEqual(sqr.size, 5)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)
        self.assertEqual(sqr.id, 1)

    def test_size_setter(self):
        """Test size setter with valid value"""
        sqr = Square(5)
        sqr.size = 7
        self.assertEqual(sqr.size, 7)
        self.assertEqual(sqr.width, 7)
        self.assertEqual(sqr.height, 5)

        with self.assertRaises(ValueError):
            sqr.size = -5

    def test_str(self):
        """Test str method"""
        sqr = Square(5, 2, 3, 1)
        self.assertEqual(str(sqr), "[Square] (1) 2/3 - 5")

    def test_update(self):
        """Test update method with args"""
        sqr = Square(5, 2, 3, 1)
        sqr.update(7, 8, 4, 5)
        self.assertEqual(sqr.id, 7)
        self.assertEqual(sqr.size, 8)
        self.assertEqual(sqr.x, 4)
        self.assertEqual(sqr.y, 5)

        sqr.update(size=12, x=6, y=7)
        self.assertEqual(sqr.size, 12)
        self.assertEqual(sqr.x, 6)
        self.assertEqual(sqr.y, 7)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        sqr = Square(5, 2, 3, 1)
        self.assertEqual(sqr.to_dictionary(), {'id': 1, 'size': 5,
                                               'x': 2, 'y': 3})


if __name__ == '__main__':
    unittest.main()
