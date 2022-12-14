#!/usr/bin/python3
"""import base from models"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherites from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of the attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getting the Width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of the width"""

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """getting the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of the Height"""

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getting the x"""

        return self.__x

    @x.setter
    def x(self, value):
        """getting x"""

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getting the y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setting the value of y"""

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """area of the rectangle"""

        return self.width * self.height

    def display(self):
        """return the rectangle from #"""

        for i in range(self.y):
            print()

        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """[Rectangle]"""

        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigning arguments"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(kwargs) != 0:

            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.width = kwargs["width"] if "width" in kwargs \
                else self.width
            self.height = kwargs["height"] if "height" in kwargs \
                else self.height
            self.x = kwargs["x"] if "x" in kwargs else self.x
            self.y = kwargs["y"] if "y" in kwargs else self.y

    def to_dictionary(self):
        """dictionary representation of rectangle"""

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
