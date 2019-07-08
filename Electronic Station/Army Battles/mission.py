# Taken from mission The Warriors

class Warrior(object):
    """klass för att lösa spelproblem checkio"""
    def __init__(self, health=50, attack=5):
##        self.health = 50
##        self.attack = attack
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

    def turn(unit_1, unit_2):
        success = False
        unit_2.health -= unit_1.attack
        p1 = unit_1.health
        p2 = unit_2.health

        if unit_1.health > 0 and unit_2.health <= 0:
            success = True
        else:

            unit_1.health -= unit_2.attack
            p1 = unit_1.health
            p2 = unit_2.health

        if unit_1.health > 0 and unit_2.health <= 0:
            success = True

        if unit_2.health <= 0:
            unit_2.is_alive = False
        if unit_1.health <= 0:
            unit_1.is_alive = False

        return success

    while unit_1.is_alive & unit_2.is_alive:
        success = turn(unit_1, unit_2)

##    success = turn(unit_1, unit_2)

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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
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

    #battle tests
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
