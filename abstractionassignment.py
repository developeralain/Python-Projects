#here we must import the abc module and abstractmethod in order to create
#abstract classes

from abc import ABC, abstractmethod

#here we define the parent abstract class, which is actually the child of the
#ABC abstract class

class mathParent(ABC):

    def Subtractionxy(self,x,y): #this is a regular method - no abstraction
        print(x - y)
  
    #here we attach @abstractmethod decorator to a method we wish to hide
    #implementation details. This also makes the Math class unable to be
    #instantiated
    
    @abstractmethod
    def Additionxy(self,x,y): pass #the pass is added so python doesn't try to run
                            #this method as it would produce an error


class mathChild(mathParent):
    
    def Additionxy(self,x,y):
        print(x + y)

xyz = mathChild()
print(xyz.Subtractionxy(5,4))
print(xyz.Additionxy(5,4))


