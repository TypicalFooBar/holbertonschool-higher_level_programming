#!/usr/bin/python3


class Square:
    __size = 0
    __position = 0

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or len(value) is not 2 or
            not isinstance(value[0], int) or not isinstance(value[1], int) or
            value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        print(self.__str__())

    def __str__(self):
        value = ""
        if self.size is 0:
            return value
        else:
            # Print empty rows for each column
            for _ in range(self.position[1]):
                value += "\n"

            for _ in range(self.size):
                # Print space ahead of each row
                for _ in range(self.position[0]):
                    value += " "
                # Print this row for the square
                for _ in range(self.size):
                    value += "#"

                value += "\n"

        return value
