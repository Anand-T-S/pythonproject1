class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printPerson(self):
        print(self.name,self.age,self.place)
f=open("person.txt","r")
for i in f:
    dt=i.rstrip("\n").split(",")
    name=dt[0]
    age=dt[1]
    place=dt[2]
    per1 = Person(name, age, place)
    per1.printPerson()
