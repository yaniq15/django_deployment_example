class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def whoAmI(self):
        print("ANIMAL")

    def eat (self):
        print("EATING")

class Dog (Animal):

    def __init__(self):
        # Animal.__init__(self)   # initialize Animal
        print('DOG CREATED')

    def eat (self):
        print("EATING dofffffffff")


my_dog= Dog()
my_dog.whoAmI()
my_dog.eat()