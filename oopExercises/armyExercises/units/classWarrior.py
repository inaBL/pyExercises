
class Warrior():
    def __init__(self):
        self.health = 50
        self.attack = 5

        self.is_alive = True


# Subclasses

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


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6


# 1-1 Duel, connects with army fights, added *args for passing Armies into function

def fight(unit_1, unit_2, *args):
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
    pass
