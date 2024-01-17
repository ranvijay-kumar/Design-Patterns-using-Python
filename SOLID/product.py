from enum import Enum

class Color(Enum):
    RED= 1
    BLUE=2
    GREEN=3

class Size(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3

class Product: 
    def __init__(self,name,color,size) -> None:
        self.name = name
        self.color=color
        self.size=size


class ProductFilter:
    def filter_by_color(self,products,color):
        for p in products:
            if p.color==color: yield p
            
    def filter_by_size(self,products,size):
        for p in  products:
            if p.size==size: yield p
    
    def filter_by_size_and_color(self,products,size,color):
        for p in products:
            if p.color==color and p.size==size:
                yield p

class Specification:
    def is_satisfied(self,item):
        pass

    def __and__(self,other):
        return AndSpecification(self,other)

class Filter:
    def filter(self, item,spec):
        pass

class ColorSpecification(Specification):
    def __init__(self,color) -> None:
        super().__init__()
        self.color=color
    
    def is_satisfied(self, item):
        return item.color==self.color

class SizeSpecification(Specification):
    def __init__(self,size) -> None:
        super().__init__()
        self.size=size
    
    def is_satisfied(self, item):
        return item.size==self.size
    

class AndSpecification(Specification):
    def __init__(self, * args) -> None:
        super().__init__()
        self.args=args
    
    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__=="__main__":
    apple=Product("Apple",Color.GREEN,Size.SMALL)
    tree=Product("Tree",Color.GREEN,Size.LARGE)
    house=Product("House",Color.BLUE,Size.LARGE)

    products=[apple,tree,house]

    pf=ProductFilter()
    print("Green products (old):")
    for p in pf.filter_by_color(products,Color.GREEN):
        print("- {item} is green".format(item=p.name))
    
    bf = BetterFilter()

    print("Green products (new):")
    green=ColorSpecification(Color.GREEN)
    for p in bf.filter(products,green):
        print("- {item} is green".format(item=p.name))


    print("Large products:")
    large=SizeSpecification(Size.LARGE)
    for p in bf.filter(products,large):
        print("- {item} is large".format(item=p.name))

    print("Large Blue products (new):")
    large_blue=large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products,large_blue):
        print("- {item} is large and blue".format(item=p.name))