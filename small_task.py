# ===============================
# Variables and Basic Operations
# ===============================

# Multiplication example
num1 = 1
num2 = 5
total = num1 * num2
print(total) 

# strings and numbers, printing with commas
name = "habiba"
age = 20     # write numbers without int, and strings without str if i use ","
country = "egypt"
print("hi my name is", name , "i'm", age, "i'm from", country)
# use "," instead of "+" 

# adding to a number variable
name = "habiba"
age = 20
x = 1 
age2 = age + x 
print("hi i'm", name, "after year your age will be", age2 )

# reassigning variables and simple addition
x = 5
x = 7
total = 5 + 7
print(total)


# ===============================
# Simple Age Checker Project
# ===============================
# This project asks the user for their name and age,
# then uses if statements to classify them:
# - If age < 13, prints "You are a child"
# - If 13 <= age <= 19, prints "You are a teenager"
# - If age >= 20, prints "You are an adult"
# Additionally, we can do simple calculations like adding 1 year to the age
name = "hanna"
age = 20
if age < 13:
   print("you are child")
elif age >= 13 and age <= 19:
   print("you are teenager")
else:
   print("you are adult")



# ===============================
# Simple Number Guessing Game
# ===============================
# This project asks the user to guess a number chosen by the computer.
# - The user inputs a number between 1 and 10.
# - The program checks the number using if/elif/else statements:
#     - If correct, prints "Correct!"
#     - If too low, prints "Too low"
#     - If too high, prints "Too high"
# It's a simple game to practice variables, input, and conditional statements.
chosen_number = 7
guess = int(input("Guess a number between 1 and 10:"))
if guess == chosen_number:
   print("correct!")
elif guess < chosen_number:
   print("Too low! Try a higher number.")
else:         # No condition here; else executes if all previous conditions fail
   print("Too high! Try a lower number.")     