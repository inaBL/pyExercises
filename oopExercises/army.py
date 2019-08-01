'''
Army, Checkio
Continuation to Duel.

The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army. Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the battle() function should return True, if the first army won, or False, if the second one was stronger.
Note that army 1 have the advantage to start every fight!


Input: The warriors and armies.
Output: The result of the battle (True or False).
Precondition: 2 types of units
'''


# From Duel exercise

class Warrior():
    def __init__(self):
        self.health = 50
        self.attack = 5

        self.is_alive = True


class Knight(Warrior):
        def __init__(self):
            super().__init__()
            self.attack = 7


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
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            break

        unit_1.health -= unit_2.attack
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

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

