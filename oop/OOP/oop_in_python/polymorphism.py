# Polymorphism

# Poly. = same method name can have multiple forms in different classes

class animal():

    def move(self):
        print("walk")
    def sound(self):
        # not implemented here → will print nothing unless overridden
        pass

class Dog(animal): 
    def move(self):
        print("run")

class snake(animal):
    def move(self):
        print("crawl")

dog1 = Dog()
snake1 = snake()

dog1.move()
snake1.move()
dog1.sound()


# In this example, the method move is defined differently in each class (Dog and Snake),
#  Every time it’s called, it shows a different behavior because we rewrote (overrode) 
# it in the subclasses.

# The method sound in the parent class has no implementation, 
# so if we call it directly, it prints nothing. But if we give it a value 
# (by overriding it in a subclass like Dog), it will output that value when called


# Unlike the previous example, here I defined the `sound` method, 
# so it will actually print a value. And of course, 
# the `sound` method inside the `Dog` class is the one that will be executed,
# not the one in the main (parent) class, 
# because Python always takes the last overridden value.



class animal():

    def move(self):
        print("walk")
    def sound(self):
        print("roar")

class Dog(animal): 
    def move(self):
        print("run")
    def sound(self):
        print("balk")

class snake(animal):
    def move(self):
        print("crawl")

dog1 = Dog()
snake1 = snake()

dog1.move()
dog1.sound()
snake1.move()