class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def draw_point(p):
    print(".",end=" ")


class Line:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.append(Line(Point(x,y),Point(x+width,y)))
        self.append(Line(Point(x+width,y),Point(x+width,y+height)))
        self.append(Line(Point(x,y),Point(x,y+height)))
        self.append(Line(Point(x,y+height),Point(x+width,y+height)))

class LineToPoint:
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return self.cache[self.h]
        print(f'Generating points for line [{line.start.x},{line.start.y}]->[{line.end.x},{line.end.y}]')
        left = min(line.start.x, line.end.x)
        right = max(line.start.x,line.end.x)
        top = max(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)
        points = []
        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left,y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x,top))
        self.cache[self.h] = points
    
    def __iter__(self):
        return iter(self.cache[self.h])




def draw(rcs):
    print("\n\n ---------------drawing some stuff---------------------\n\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPoint(line)
            for p in adapter:
                draw_point(p)



if __name__ == "__main__":
    rs = [
        Rectangle(1,1,10,10),
        Rectangle(3,3,6,6)
    ]
    draw(rs)