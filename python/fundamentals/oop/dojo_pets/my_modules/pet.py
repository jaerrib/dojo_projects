class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100

    def sleep(self):
        if self.energy <= 75:
            self.energy += 25
        return self

    def eat(self):
        if self.energy <= 95:
            self.energy += 5
        if self.health <= 90:
            self.energy += 10
        return self

    def play(self):
        if self.health <= 95:
            self.energy += 5
        return self

    def noise(self):
        print("Pet's sound")