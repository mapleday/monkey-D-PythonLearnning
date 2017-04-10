#Give any animal you want
class animalFactory:
    def __init__(self,name="cat",age=2,weight=20.0):
        self.name=name
        self.age=age
        self.weight=weight
    def animal(self):
        print self.name+'\t'+str(self.age)+'\t'+str(self.weight)
        return self