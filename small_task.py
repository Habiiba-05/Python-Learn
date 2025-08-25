# Basic Operations

# strings and numbers, printing with commas
name = "habiba"
age = 20    
country = "egypt"
print("hi my name is", name , "i'm", age, "i'm from", country)

# adding to a number variable
name = "habiba"
age = 20
x = 1 
age2 = age + x 
print("hi i'm", name, "after year your age will be", age2 )

# Convert the user's input from a string to an integer, Line 35
# Without this, you can't perform math operations.
# when printing, we must convert numbers to string using str() 
oranges_input = input("how many oranges did you take?")
oranges_num = 5
taken_oranges = oranges_num - int(oranges_input)     
print("number of oranges currently is " + str(taken_oranges))



