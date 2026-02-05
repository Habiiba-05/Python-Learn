# Inheritance


# Dog and Snake are subclasses of Animal (the parent class)
# That means they automatically inherit any methods defined in Animal
# So:
# 1- If they don’t override a method → they use the one from Animal
# 2- If they override a method → their own version runs instead


# Case 1
class animal():

    def move(self):
        print("walk")
    def sound(sele):
        pass

class Dog(animal):
    pass

class snake(animal):    
    def move(self):
        print("crawl")

dog1 = Dog()
snake1 = snake()

dog1.move()
snake1.move()




# Case 2
class animal():

    def move(self):
        print("walk")
    def sound(sele):
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


