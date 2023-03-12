#..............Abstract Base class nd @abstractmethod..............

#from abc import ABCMeta, abstractclassmethod
from abc import ABC, abstractclassmethod

class shape(ABC):
    @abstractclassmethod
    def printarea(self):
        return 0

class Rectangle(shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=7
        self.breadth=8
    
    def printarea(self):
        return self.length*self.breadth


rec1=Rectangle()
print(rec1.printarea())