class Dog():
    # CLASS OBJECT ATTRIBUTE

    species = "mamal"
    def __init__(self, breed, name):
        #CLASS OBJECT ATTRIBUTE

        species="mamal"

        self.breed = breed
        self.name=name


my_dog = Dog("LAB", "Milou")
print(my_dog.breed)
my_otherdg =Dog("LIL", "dougi")

print(my_dog.name)
print(my_dog.species)


