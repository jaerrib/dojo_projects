class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )

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

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method


class Pet:
    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100

    def sleep(self):
        if self.energy < 75:
            self.energy += 25
        else:
            self.energy = 100
        return self

    def eat(self):
        if self.energy < 95:
            self.energy += 5
        else:
            self.energy = 100
        if self.health < 90:
            self.energy += 10
        else:
            self.energy = 100
        return self

    def play(self):
        if self.health < 95:
            self.energy += 5
        else:
            self.energy = 100
        return self

    def noise(self):
        print("Pet's sound")


ninja = Ninja(
    "Jackie",
    "Chan",
    ["kibbles", "bits"],
    5,
    Pet(
        "Mr. Pickles",
        "Guinea Pig",
        ["roll over", "dance"]))

# ninja.feed()

ninja.feed().walk().bathe()
