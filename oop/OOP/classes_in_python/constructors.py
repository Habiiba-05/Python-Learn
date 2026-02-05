# constructors

# Define a class called circle
# A class is like a blueprint: it defines how to create objects (instances) with specific data and behavior

class circle():

# Constructor (__init__ method)
# It takes the radius (r) as a parameter and stores it in the object (self.r)

    def __init__(self, r):
        self.r = r
    def diameter(self):
        d = 2 * self.r
        print(f'diameter equals {d}')

my_circle = circle(7)
my_circle.diameter()
print(my_circle.r)

my_circle2 = circle(3)
my_circle2.diameter()
print(my_circle2.r)



# Encapsulation in Python means hiding the data or the internal details of a class 
# and controlling how people interact with it from the outside.