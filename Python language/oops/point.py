class Point:
    def __init__(self,x=0,y=0) -> None:
        self.x=x
        self.y=y
    
    def __str__(self) -> str:
        '''String representation of point'''
        return f'This is a point with coordinate abscissa {self.x} and ordinate {self.y}'
    
    def __repr__(self) -> str:
        '''Point init method'''
        return f'Point(x={self.x},y={self.y})'
    
    def __add__(self,right):
        '''Override + operator and do point adding and return a new instance'''
        return Point(self.x+right.x,self.y+right.y)

    def __mul__(self,factor):
        '''Override * operator and do point adding and return a new instance'''
        return Point(self.x*factor,self.y*factor)

if __name__=="__main__":
    p1 = Point()
    print(p1)      # (0.00, 0.00)
    p1.x = 5
    p1.y = 6
    print(p1)      # (5.00, 6.00)
    p2 = Point(3, 4)
    print(p2)      # (3.00, 4.00)
    print(p1 + p2) # (8.00, 10.00) Same as p1.__add__(p2)
    print(p1)      # (5.00, 6.00) No change
    print(p2 * 3)  # (9.00, 12.00) Same as p1.__mul__(p2)
    print(p2)      # (9.00, 12.00) Changed
