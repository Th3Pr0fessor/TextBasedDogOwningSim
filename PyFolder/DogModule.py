import time

class Dog():

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.hunger = 100
        self.thirst = 100
        self.enjoyment = 100

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")

    def thirst(self, gain):
        if gain:
            self.thirst = self.thirst + 2
        elif not gain:
            self.thirst = self.thirst - 1

    def hunger(self, gain):
        if gain:
            self.hunger = self.hunger + 2
        elif not gain:
            self.hunger = self.hunger - 1

    def enjoyment(self, gain):
        if gain:
            self.enjoyment = self.enjoyment + 2
        elif not gain:
            self.enjoyment = self.enjoyment - 1

    def statPrinter(self):
        print(self.hunger)
        print(self.thirst)
        print(self.enjoyment)



