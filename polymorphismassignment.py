##Create two classes that inherit from another class.
##
##
##Each child should have at least two of their own attributes.
##
##The parent class should have at least one method (function).
##
##Both child classes should utilize polymorphism on the parent class method.
##
##Add comments throughout your Python explaining your code.


#parent class created
class WoWPlayer():
    Name = 'Alain'
    Email = 'alain@gmail.com'
    Password = 'sillyhats123'
#function that prints certain attributes of parent
    def PlayerInfo(self):
        msg = '\nPlayer Name: {}\nPlayer Email: {}'.format(self.Name,self.Email)
        return msg
    
#child class created
class Rogue(WoWPlayer):
    Class = 'Rogue'
    Level = 60
    Specialization = 'Subtlety'
    Weapons = ['Chromatically Tempered Sword','Maladath']
    Armor = ['Bloodfang Regalia','Master Dragonslayer Ring']
    Agility = 391
    Dodge = '30%'
#polymorphism of parent function of same name. Some printed data identical to
#parent and some different
    def PlayerInfo(self):
        msg = '\nPlayer Name: {}\nClass: {}\nLevel: {}\nSpec: {}'.\
              format(self.Name,self.Class,self.Level,self.Specialization)
        return msg
    
#another child class is created
class Warrior(WoWPlayer):
    Class = 'Warrior'
    Level = 60
    Specialization = 'Arms'
    Weapons = ['Ashkandi, Greatsword of the Brotherhood']
    Armor = ['Field Marshal\'s Armaments','Marshal\'s Boots']
    Strength = 455
    Crit = '31%'
#polymorphism of parent function of same name. Some printed data identical to
#parent and some different
    def PlayerInfo(self):
        msg = '\nPlayer Name: {}\nClass: {}\nLevel: {}\nSpec: {}'.\
              format(self.Name,self.Class,self.Level,self.Specialization)
        return msg

#if this script is run from this page, then its __name__ will be __main__
#and therefore the functions blow will run. Otherwise, they will not run.
if __name__ == '__main__':

#Below are instantiations of the parent and two children. Below are also 3
#functions of the same name, two of which are polymorphisms of the parent\'s
#function. 
    Player = WoWPlayer()
    print(Player.PlayerInfo())
    
    Silentstab = Rogue()
    print(Silentstab.PlayerInfo())

    Criticalz = Warrior()
    print(Criticalz.PlayerInfo())

    
    
