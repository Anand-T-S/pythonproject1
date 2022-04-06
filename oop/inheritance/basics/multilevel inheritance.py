class A:
    def methodA(self):
        print("inside method A")
class B(A):
    def methodB(self):
        print("inside method B")
class C(B):
    def methodC(self):
        print("inside method C")
c=C()
c.methodA()
c.methodB()
c.methodC()

b=B()
b.methodB()
b.methodA()