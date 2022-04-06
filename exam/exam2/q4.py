class Animals:
    def __init__(self,type):
        self.type=type
    def printanimal(self):
        print(self.type)
class Dog(Animals):
    def __init__(self,type,name,breed):
        super().__init__(type)
        self.name=name
        self.breed=breed
    def printdog(self):
        print(self.type,self.name,self.breed)
d1=Dog("Mammals","jack","rottweiler")
d1.printdog()