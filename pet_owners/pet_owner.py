from pet import Pet, Dogs

class Human:
    def __init__(self, first_name, last_name, pet, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self. treats = treats
    def walk(self):
        print(f'Walking {self.pet.name}')
        return self
    def feed(self):
        self.pet.eat()
        print(f"Pet's health: {self.pet.health}, Pet's energy: {self.pet.energy}")
        return self
    def bathe(self):
        self.energy += 5
        print(f"Pets energy: {self.pet.energy}")
        return self



# pet_1 = Pet("Benny", "Cat", "loaf", 100, 0)
# owner_1 = Human("Miguel", "Mozo", pet_1, ["bacon bits", "chicken bits"])

# owner_1.walk().feed()


pet_2 = Pet("Chuck", Dogs, "sit", 100, 80)
owner_1_dogs = Human("Miguel", "Mozo", pet_2, "dog treat")
owner_1_dogs.walk().feed()
