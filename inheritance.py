class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

mydog = Dog()
mydog.who_am_i()
mydog.eat()

myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()
