# Some data types
print(type(10))                               # int - integer number
print(type(100.99))                           # float - floating point number
print(type("hello"))                          # str - string
print(type([1, 2, 3, 4]))                     # list
print(type((1, 2, 3, 40)))                    # tuple
print(type(2 == 2))                           # bool - True
print(type(2 == 4))                           # bool - False
print(type({"one": 1, "two": 2}))             # dict - dictionary (key-value pairs)

# When we use type(), the output will be the variable’s type, not its value
x = 10
y = "python"
print(type(x))
print(type(y))

# Variable Naming Styles
name = 10                                     # normal
print(name)

myVariableName = "hi"                         # camelCase
print(myVariableName)

my_variable_name = 3.02                       # snake_case
print(my_variable_name)

MyVariableName = "john"                       # PascalCase
print(MyVariableName)

# This program asks the user for their name and then prints a greeting.
name = input("what's your name")
print("my name is " + name) 

# Strings can be enclosed in either double or single quotes
x = "John"
x = 'John'

# Allow multiple variables in one line
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# This is called unpacking
fruits = ["banana", "cherry", "mango"]
x, y, z = fruits
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = 10
print(x)
print(y)
print(z)

# Global variable example
x = "successful"
def myfunc():
    print("I'm " + x)
myfunc()

# Using the global keyword to modify a global variable
def book():
    global x
    x = "shatter me"
book()
print("I'm reading", x)

x = "power of now"
def book():
    global x
    x = "shatter me"
book()
print("I love reading power of now more than", x)

# Example without global keyword
# Output will be "Python is awesome" because there is no global keyword
x = 'awesome'
def myfunc():
    x = 'fantastic'
myfunc()
print('Python is ' + x)