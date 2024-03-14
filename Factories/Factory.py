from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self,a,b,system=CoordinateSystem.CARTESIAN) -> None:
    #     if system==CoordinateSystem.CARTESIAN:
    #         self.x=a
    #         self.y=b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = b * sin(b)

    def __init__(self,x=0,y=0) -> None:  
        self.x=x
        self.y=y
    
    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        def cartesian_point(self,x,y):
            return Point(x,y)
        
    
        def new_polar_point(self,rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))
        
    factory = PointFactory()
    
if __name__=="__main__":
    p = Point(2,3)
    p2 = Point.factory.new_polar_point(1,2)
    print(p)
    print(p2)
    

    