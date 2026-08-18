from random import randint
from math import floor


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):

        dice_numbers = []
        for _ in range(4):
            dice_numbers.append(randint(1, 6))

        dice_numbers.pop(dice_numbers.index(min(dice_numbers)))

        return sum(dice_numbers)


def modifier(value):
    return floor((value - 10) / 2)
