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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Returns the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Checks and sets the width of the Rectangle
        value (int): The width of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Checks and sets the height of the Rectangle
        value (int): The height of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of a Rectangle.
        Returns:
            int: The area of a Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """
        Computes the perimeter of a Rectangle.
        Returns:
            int: The perimeter of a Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def draw_rec(self):
        """
        Draw the Rectangle with their size
        Returns:
            str: `Empty` If width or height is `0`,
            otherwise returns a string with the Rectangle.
        """

        w = self.__width
        h = self.__height
        base = ''
        
        if w == 0 or h == 0:
            return base

        for i in range(w):
            for a in range(h):
                return base += #

        if i != h - 1:
            rect_str += '\n'
                
    def __str__(self):
        """
        Returns a string with the representation of the Rectangle.
        """
        return __draw_rec()
