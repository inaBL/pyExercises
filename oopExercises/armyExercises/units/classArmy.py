from .classWarrior import *


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, warrior_type, number):
        i = 0
        try:
            while i < number:
                if warrior_type == Warrior:
                    self.units.append(Warrior())
                elif warrior_type == Knight:
                    self.units.append(Knight())
                elif warrior_type == Defender:
                    self.units.append(Defender())
                elif warrior_type == Vampire:
                    self.units.append(Vampire())
                elif warrior_type == Lancer:
                    self.units.append(Lancer())
                i += 1
        except TypeError:
            print('You can only add Warrior types, for more information and subtypes see classWarrior.py')


class Battle():
    def __init__(self):
        pass

    # army battle
    def fight(self, army1, army2):
        while len(army1.units) > 0 and len(army2.units) > 0:
            if fight(army1.units[0], army2.units[0]):
                army2.units.pop(0)
            else:
                army1.units.pop(0)

        return len(army1.units) > 0


if __name__ == '__main__':
    pass
