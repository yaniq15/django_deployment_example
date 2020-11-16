class CIRCLE():
    pi=3.14
    def __init__(self, radius=1):
        self.radius =radius
    def area(self):
        return self.radius*self.radius * CIRCLE.pi

    def set_radius(self, new_r):
        self.radius=new_r

my_c =CIRCLE(3)
print(my_c.radius)
# my_c.radius=100
my_c.set_radius(11)
print(my_c.area())