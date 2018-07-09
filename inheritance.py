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

    def bark(self):
        print("BORK BORK")

mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()

myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()
