'''
Vampires, Checkio.

So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter, which helps him to heal himself. When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).

The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

Input: The warriors and armies.
Output: The result of the battle (True or False).
Precondition: 4 types of units
'''


# From Defenders exercise
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


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4

    def vampirism(self, dmg):
        self.health += float(0.5 * dmg)


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
            if isinstance(unit_1, Vampire):
                unit_1.vampirism(unit_1.attack - unit_2.defence)
            if unit_2.health <= 0:
                unit_2.is_alive = False
                break

        if unit_1.defence < unit_2.attack:
            unit_1.health -= unit_2.attack - unit_1.defence
            if isinstance(unit_2, Vampire):
                unit_2.vampirism(unit_2.attack - unit_1.defence)
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
