class Dog():

    def __init__(self, breed, name):
        self.breed = breed
        self.name =name

mydog = Dog(breed = "Lab", name = "Dale")
otherdog = Dog(breed = "Husky", name = "Aspen")

print(mydog.breed)
print(mydog.name)
print(otherdog.breed)
print(otherdog.name)
