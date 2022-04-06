# multiple  inheritance
# child class have more than one parent

class A:
    def methoda(self):
        print("inside a")
class B:
    def methodb(self):
        print("inside b")
class C(A,B):
    def methodc(self):
        print("inside c")
c=C()
c.methoda()
c.methodb()
c.methodc()