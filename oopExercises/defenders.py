'''
Defenders, Checkio.

Let's add another one - the Defender. It should be the subclass of the Warrior class and have an additional defense parameter, which helps him to survive longer. When another unit hits the defender, he loses a certain amount of his health according to the next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.

The basic parameters of the Defender:
health = 60
attack = 3
defense = 2
'''


# From Army exercise
class Warrior():
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0

        self.is_alive = True


class Knight(Warrior):
        def __init__(self):
            super().__init__()
            self.attack = 7


# New addition, Defender
class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, warrior_type, number):
        i = 0
        try:
            if warrior_type == Warrior:
                while i < number:
                    self.units.append(Warrior())
                    i += 1
            elif warrior_type == Knight:
                while i < number:
                    self.units.append(Knight())
                    i += 1
            elif warrior_type == Defender:
                while i < number:
                    self.units.append(Defender())
                    i += 1
        except TypeError:
            print('You can only add Warrior or Knight')


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


# 1-1 duel
def fight(unit_1, unit_2):
    while True:
        if unit_2.defence < unit_1.attack:
            unit_2.health -= unit_1.attack - unit_2.defence
            if unit_2.health <= 0:
                unit_2.is_alive = False
                break

        if unit_1.defence < unit_2.attack:
            unit_1.health -= unit_2.attack - unit_1.defence
            if unit_1.health <= 0:
                unit_1.is_alive = False
                break

    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

