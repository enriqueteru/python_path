from distutils.log import debug
from sre_parse import State


class Player:

    # class variable shared by all instances
    def __init__(self, name):
        self.name = name
        self.state = 'alive'
        self.powers = []
        self.life = 100
        
    def __add_power(self, power):
       self.powers.append(power)
        
    def tell_storie(self):
        print('You are ' + self.name + ' have powers like ' + str(*self.powers))
        
    def set_strike(self, hit):
        print('hit power ' + str(hit))
        self.life -= hit
        
        if(self.life <= 0):
            self.life = 0
            self.state = 'Dead'
            return self.get_health() 
             
    def set_powers(self, power):
        self.__add_power(power)
        
    def get_health(self):
        return  self.life
    
    def get_state(self):
        return  self.life
        
    def get_powers(self):
        print(self.powers)      
        
        
   
    