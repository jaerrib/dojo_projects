class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if self.pet_food > 0:
            self.pet_food -= 1
            self.pet.eat()
        else:
            print("Oh no!! You need more pet food!")
        return self

    def bathe(self):
        self.pet.noise()
        return self
