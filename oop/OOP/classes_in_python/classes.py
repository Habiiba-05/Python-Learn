# Classes 

# Define a class called Color
# A class is like a "blueprint" that we can use to create multiple objects
# Each object can have behaviors (methods) and attributes (variables)

class color():

    def black(self):
        print("black")

    def red(self):
        print("red")
# Method called red
# Prints "red" → the first parameter must always be 'self' (represents the object itself)

        
# Create the first object (instance) from the class        
my_color = color()
my_color.black()
my_color.red()

# Add a new attribute to the object dynamically
# In Python, you can add new attributes to objects at runtime
my_color.blue = "blue"
print(my_color.blue)

# Create another object from the same class
color2 = color()
color2.black()
color2.green = "green"    # Add a different attribute to the second object
print(color2.green)