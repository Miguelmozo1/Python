class Pet:
    def __init__(self, name, type, commands, health, energy):
        self.name = name
        self.type = type
        self.commands = commands
        self.health = health
        self.energy = energy
    def sleep(self):
        self.health += 5
        self.energy += 5
    def eat(self):
        self.health += 10
        self.energy += 15
    def play(self):
        self.health += 5
        self.energy -= 10


class Dogs(Pet):            # inheritance
    def __init__(self):
        super().__init__(type)
        self.type = "Dog"
        return self