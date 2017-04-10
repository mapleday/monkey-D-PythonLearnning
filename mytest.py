#the first Python script
def multiply(x,y):
    try :
        ret = x * y
    except StandardError:
        ret =0
    return ret

s = multiply(3,4)
print s

#test atom class
import atom
a=atom.AtomClass(2.0,Element='O',Mass=16.0)
b=atom.AtomClass(1.0)
print a.Element
print a.Mass
print a.Momentum()
print b.Element
print b.Velocity

import animalFactory
animal=animalFactory.animalFactory("dog",3,1.5)
animal.animal()
print "the first python program!"
