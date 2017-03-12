
# modules and packages
# module ends in .py
# https://www.youtube.com/watch?v=aJeb1j_dlOA&t=1s

import sys
import os
from myMudule import Person

from myPackage.Car import *

person1 = Person()
person1.name = "Brayn"
person1.sayHello()

myCar = Car()
myCar.setSpeed(100)

myTruck = Truck()
myTruck.setSpeed(90)

print sys.version
print (dir(os))