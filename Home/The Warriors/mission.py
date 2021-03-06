class Warrior(object):
    """klass för att lösa spelproblem checkio"""
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        if self.health > 0:
            self.is_alive = True
        else:
            self.is_alive = False

    def talk(self):
        print("Health = " + str(self.health))
        print("Attack = " + str(self.attack))
        print("I liv = "  + str(self.is_alive))
    pass

class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        self.health = health
        self.attack = attack
        if self.health > 0:
            self.is_alive = True
        else:
            self.is_alive = False
    pass

def fight(unit_1, unit_2):
    success = False
    while unit_1.is_alive & unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_1.health > 0 and unit_2.health <= 0:
            success = True
        else:
            unit_1.health -= unit_2.attack
        if unit_1.health > 0 and unit_2.health <= 0:
            success = True
        if unit_2.health <= 0:
            unit_2.is_alive = False
        if unit_1.health <= 0:
            unit_1.is_alive = False
    return success

if __name__ == '__main__':

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

    print("Coding complete? Let's try tests!")
