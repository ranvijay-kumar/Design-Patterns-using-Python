#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""circle.py: The circle module, which defines the Circle class"""
from math import pi
 
class Circle:
    """A Circle instance models a circle with a radius"""
 
    def __init__(self, _radius = 1.0):
        """Initializer with default radius of 1.0"""
        # Change from radius to _radius (meant for internal use)
        # You should access through the getter and setter.
        self.radius=_radius   # Call setter
 
    def set_radius(self, _radius):
        """Setter for instance variable radius with input validation"""
        if _radius < 0:
            raise ValueError('Radius shall be non-negative')
        self._radius = _radius
 
    def get_radius(self):
        """Getter for instance variable radius"""
        return self._radius
 
    def get_area(self):
        """Return the area of this Circle instance"""
        return self.get_radius() * self.get_radius() * pi  # Call getter
    
    radius = property(get_radius, set_radius)
 
    def __repr__(self):
        """Return a command string to recreate this instance"""
        # Used by str() too as __str__() is not defined
        return 'Circle(radius={})'.format(self.get_radius())  # Call getter
 
if __name__ == '__main__':
    c1 = Circle(1.2)

    # Access (read/write) the new property radius directly
    print(c1.radius)    # Run get_radius() to read _radius
                        #1.2
    c1.radius = 3.4     # Run set_radius() to change _radius
    print(c1.radius)    # Run get_radius() to read _radius
                        #3.4
    print(vars(c1))     #{'_radius': 3.4}
    print(dir(c1))      #['_radius', 'get_radius', 'radius', 'set_radius', ...]

    # The existing instance variable _radius, getter and setter are still available
    c1._radius = 5.6
    print(c1._radius)       #5.6
    c1.set_radius(7.8)
    print(c1.get_radius())  #7.8

    print(type(c1.radius))       #<class 'float'>
    print(type(c1._radius))      #<class 'float'>
    print(type(Circle.radius))   #<class 'property'>
    print(type(Circle._radius))  #AttributeError: type object 'Circle' has no attribute '_radius'