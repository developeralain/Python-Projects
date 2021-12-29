
#this defines the Player parent class. It has attributes that all children
#will possess. The 'Player' here is supposed to represent a video game player
#for an RPG game that features classes such as mages and warriors.
class Player:
    user_name = 'JacobRules'
    password = '1234234f'
    email = ' '
    server_type = 'Please choose PVP or PVE'
    character_name = ' '
    race = ' '
    gender = ' '
    health = '100'
    
#this is the first child of parent Player. Only mages have spell power and mana.
#it will posses all traits of the player parent as these apply.
class Mage(Player):
    spell_power = '100'
    mana = '80'
    
#this is the second child of a parent Player. Only warriors have rage as a
#resource and only they use weapons. 
class Warrior(Player):
    rage = '0'
    weapon = 'sword of the bear'

#here you can designate a mage as 'Evandros' and instantiate him.
Evandros = Mage
#here you can see what his starting mana pool is
print(Evandros.mana)
#here you can see the username is carried over from parent class Player
print(Evandros.user_name)

#here you can designate a warrior as 'Savages'
Savages = Warrior
#here you can see what his starting weapon is
print(Savages.weapon)
#here you can see the username is carried over from parent class Player
print(Savages.user_name)
