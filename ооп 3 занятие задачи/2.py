class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Predator(Animal):
    def bit(self, victim):
        if isinstance(victim, Mammal) == True:
            victim.die()

class Tiger(Predator):
    pass

class Mammal(Animal):
    def die(self):
        del self

class Zebra(Mammal):
    pass
tiger = Tiger('Tiger', 5)
zebra = Zebra('Zebra', 4)
tiger.bit(zebra)
