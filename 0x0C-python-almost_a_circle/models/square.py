#!/usr/bin/python3
"""Module contains class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining class square that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute"""
        self.width = value

    def __str__(self):
        """Return string representation of the Square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Method that assigns attributes"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if attrs[i] == 'size':
                    self.width = arg
                    self.height = arg
                else:
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        attrs = ['id', 'size', 'x', 'y']
        dcy = {}

        for key in attrs:
            if key == 'size':
                dcy[key] = getattr(self, 'width')
            else:
                dcy[key] = getattr(self, key)

        return dcy
