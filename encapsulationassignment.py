#chicken class is created
class Chicken:
    def __init__(self):#a function that allows initialization of a chicken object
        self._varPeck = "I have pecked the ground in search of seeds and worms"
        self.__varFly = "The chicken attempts to fly, but fails miserably"

    def pecker(self):#function that prints _varPeck variable
        print(self._varPeck)

    def flyer(self):#function that prints __varFly variable
        print(self.__varFly)

    def changeFlight(self,flight): #function that allows user to pass new values
                                    #into __varFly variable
        self.__varFly = flight
        

Flightmaster = Chicken()#Chicken class initialized as object stored in Flightmaster
Flightmaster.pecker()#prints _varPeck
Flightmaster.flyer()#prints __varFly
Flightmaster.changeFlight("The chicken tries hard--real hard--and then fails.")#changes __varFly value
Flightmaster.flyer()#prints new __varFly value


    
