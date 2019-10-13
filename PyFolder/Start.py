from DogModule import Dog

name = input("What is your desired dog name?\n")
my_dog = Dog(name, 6, "Pincher")
day = 0


def statloss(pet):
    pet.enjoymentfunc(False)
    pet.thirstfunc(False)
    pet.hungerfunc(False)


def nextDay(pet):
    global day
    pet.statPrinter()
    print(day)
    dec = input("What do you want to do now? Your options are... \n Next \n Play \n Quench \n Feed \n")
    print(dec)
    statloss(pet)
    if dec == "Next":
        day = day + 1
        nextDay(pet)
    elif dec == "Play":
        pet.enjoymentfunc(True)
        nextDay(pet)
    elif dec == "Feed":
        pet.hungerfunc(True)
        nextDay(pet)
    elif dec == "Quench":
        pet.thirstfunc(True)
        nextDay(pet)
    else:
        print("You wasted a day")
        nextDay(pet)


nextDay(my_dog)
