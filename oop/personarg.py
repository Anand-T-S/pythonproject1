class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
per1=Person()
per1.setvalue("anu",21,"kochi")
per1.printvalue()

per2=Person()
per2.setvalue("amal",23,"tcr")
per2.printvalue()