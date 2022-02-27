from abc import ABC, abstractmethod

class Clothing(ABC):
    name = None

    @abstractmethod
    def __str__(self):
        pass

class Coat(Clothing):
    name = 'пальто'

    def __init__(self, v):
        self.v = v

    def __str__(self):
        return '[' + self.name +  ' размера '  + str(self.v) +  ']'

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothing):
    name = 'костюм'

    def __init__(self, h):
        self.h = h

    def __str__(self):
        return '[' + self.name + ' размера ' + str(self.h) + ']'

    @property
    def consumption(self):
        return 2 * self.h + 0.3


coat = Coat( 52 )
suit = Suit( 181 )

print( coat, '; ткани надо:', coat.consumption )
print( suit, '; ткани надо:', suit.consumption )
print('Общий расход ткани:', coat.consumption + suit.consumption)

