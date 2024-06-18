from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    @property
    def length(self):
        return self.__length
    
    @property
    def width(self):
        return self.__width
    
    @property
    def area(self):
        return self.length * self.width
    
    @property
    def perimeter(self):
        return (self.length + self.width) * 2
    

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side
    
    @property
    def area(self):
        return self.side * self.side
    
    @property
    def perimeter(self):
        return self.side * 4
    
class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius):
        self.__major_radius = major_radius
        self.__minor_radius = minor_radius
    
    @property
    def major_radius(self):
        return self.__major_radius
    
    @property
    def minor_radius(self):
        return self.__minor_radius
    
    @property
    def area(self):
        return pi * self.minor_radius * self.major_radius
    
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def area(self):
        return pi * self.radius ** 2
    
    @property
    def perimeter(self):
        return 2 * pi * self.radius
    
    