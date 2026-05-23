"""Tasks 9-13 to 9-15 (Python Crash Course)"""
from random import randint

# 9-13 Refactoring with OrderDict
from collections import OrderedDict

glossary = OrderedDict({
        'Kosta': "Alimov",
        'Nyasha':"Malysheva",
        'Vladimir': "Putin",
        'Yarik': "Alimov",
        'Varvar':"Alimova"
        }
)
for key, value in glossary.items():
    print(f"\n{key.title()}'s surname - {value}")


# 9-14 Dices

class Dice():
    """Describes a Dice"""
    def __Init__(self):
        """Constructor"""
        self.sides = 6
        self.current_side = 1

    def roll(self):
        "Rolls a dice and outputs result"
        print(f'Rolling dice 1d{str(self.sides)} ...')
        self.current_side = randint(1,self.sides)
        print(f'Dice shows {self.current_side}!')

d20 = Dice()
d20.sides = 20
d20.roll()



