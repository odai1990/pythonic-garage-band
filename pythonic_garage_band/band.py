from abc import abstractmethod
from typing import ClassVar

class Band:
    instances = []
    def __init__(self,name,members ):
        self.name=name
        self.members =members
        Band.instances.append(self) # Increment the count everytime we create a Pet (Cat or Dog) 
       

    def play_solos(self):
        return list(map(lambda i:i.play_solo(), self.members))


    def __str__(self):
        return f'this is the band class'

    def __repr__(self):
        return f'this is the object{self}'

    @classmethod
    def to_list(cls):
        return cls.instances
    

class Musician:

    def __init__(self,name):
        self.name=name  



    @abstractmethod
    def get_instrument(self):
        pass


    @abstractmethod
    def play_solo(self):
        pass


    @abstractmethod
    def get_instrument(self):
        pass


    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):


    def __str__(self):
         return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):


    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
       return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'bass'


    def play_solo(self):
        return 'bom bom buh bom'

        
class Drummer(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
       return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return 'drums'
    
    def play_solo(self):
        return 'rattle boom crash'





