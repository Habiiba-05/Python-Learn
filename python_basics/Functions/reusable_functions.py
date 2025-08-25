# Re-Usable functions

# Function to check if a number is 
 # If the remainder when dividing by 2 is 0, the number is even
# Otherwise, it is odd
def is_even(num):
    if(num % 2 == 0):           
          return "even"
    return "odd"

# Call the function with 6 -> should return "even"
print(is_even(6))             



# OR 

# Function that always returns "odd" (not a real check, just an example)
def is_odd(num):
     return "odd" 

print(is_odd(7))



# Lab: Write a function to return % of exam grade
def grade_in_percent(grade, fullmark):
    return grade / fullmark * 100

gradepercent = grade_in_percent(73,75)
print( f'the grade is {gradepercent} %')