class Unit :
    # __init__ is a constructor
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[Unit moves]")
        print("{0} is now moving in direction of {1}. [ speed {2} ]"\
            .format(self.name, location, self.speed))

# classname(UpperClass) : inheritance
class AttackingUnit(Unit) :
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name, hp, speed)
        self.damage = damage
        print(f"{self.name} Unit has been spawned.")
        print(f"HP {hp}, damage {damage}")
    
    def attack(self, location):
        print("{0} is attacking in direction of {1}. [ Damage : {2} ]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} has {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} has {1} hp.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} has been destroyed".format(self.name))

class Flyable:
    def __init__(self, speed):
        self.speed = speed
    
    def fly(self, name, location):
        print(f"{name} is heading {location} [ Speed : {self.speed} ]")

# multi-inherit
class FlyableAttackUnit(AttackingUnit, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackingUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, speed)
    def move(self, location):
        print("Unit flying")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) # Reaching to paraent class, Use it without self
        self.location = location


vulture = AttackingUnit("Vulture", 80, 10, 20)
battlecruiser = FlyableAttackUnit("BattleCruiser", 500, 25 ,3)
vulture.move("11 o'clock")
battlecruiser.move("9 o'clock")