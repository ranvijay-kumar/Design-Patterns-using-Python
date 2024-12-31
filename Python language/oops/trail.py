class A:
    def rk(self):
        print(" In class A")
class B(A):
    pass
class C(A):
    def rk(self):
        print("In class C")
 
# classes ordering
class D(B, C):
    pass
    
r = D()
r.rk()