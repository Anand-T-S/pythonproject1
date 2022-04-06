# single inheritance ...one parent class for child
class A:
    def methoda(self):
        print("inside method a")
class B(A):    #child class/sub class/derived class
    def methodb(self):
        print("inside method b")
a=A()
a.methoda()
b=B()
b.methodb()
b.methoda()