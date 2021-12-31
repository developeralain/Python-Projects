class Chicken:
    def __init__(self):
        self._varPeck = "I have pecked the ground in search of seeds and worms"
        self.__varFly = "The chicken attempts to fly, but fails miserably"

    def pecker(self):
        print(self._varPeck)

    def flyer(self):
        print(self.__varFly)

    def changeFlight(self,flight):
        self.__varFly = flight
        

Flightmaster = Chicken()
Flightmaster.pecker()
Flightmaster.flyer()
Flightmaster.self_varPeck = "I pecked your nose"
Flightmaster.changeFlight("The chicken tries hard--real hard--and then fails.")
Flightmaster.flyer()

    
