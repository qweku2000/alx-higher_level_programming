#!/usr/bin/python3
"""
A module with a Rectangle that does nothing
"""

class Rectangle:
    """ An empty rectangle class """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width=width
        self.height=height

    @property
    def width(self):
        """
        Returns the width of the Rectangle
        """
        return self.__width
    @width.setter
    def width(self,value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @height.getter
    """
    Returns the width of the Rectangle
    """

    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
         if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
