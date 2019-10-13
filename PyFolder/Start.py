from DogModule import Dog

name = input("What is your desired dog name? ")
my_dog = Dog(name, 6, "Pincher")
day = 0


def statloss(Dog):
    Dog.looseEnjoyment
    Dog.looseHunger()
    Dog.looseThirst()


def NextDay(pet):
    global day
    pet.statPrinter()
    print(day)
    dec = input("What do you want to do now? ")
    print(dec)
    pet.enjoyment(False)
    pet.thirst(False)
    pet.hunger(False)
    if dec == "Next":
        day = day + 1
        NextDay(pet)
    elif dec == "Play":
        pet.enjoyment(True)
        NextDay(pet)


NextDay(my_dog)
