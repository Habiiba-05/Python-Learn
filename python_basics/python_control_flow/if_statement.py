# IF statement

if 1<8:                     #don't forget semicolon
   print("one is less than eight")       #indentation soooo must



name = "hanna"
age = 20
if age < 13:
   print("you are child")
elif age >= 13 and age <= 19:
   print("you are teenager")
else:
   print("you are adult")



chosen_number = 7
guess = int(input("Guess a number between 1 and 10:"))
if guess == chosen_number:
   print("correct!")
elif guess < chosen_number:
   print("Too low! Try a higher number.")
else:         # No condition here; else executes if all previous conditions fail
   print("Too high! Try a lower number.")     



is_student = True
is_grad = False
if is_student:
   print("welcome inside!")
elif is_grad:
   print("congrats!")
else:
   print("you can not come inside.")



# Logical operations:
# There are 3 logical operators in Python: and, or, and not

# AND - Returns True if both operands are true 
is_man = True
is_parent = True
if is_man and is_parent:
   print("man and parent")
else:
   print("not man or perant")

# OR - Returns True if at least one of the operands is true
is_man = True
is_parent = False
if is_man or is_parent:
   print("man")
else:
   print("not man or perant")

# NOT - Returns True if the operand is false, and vice versa
is_man = True
is_parent = False
if is_man and not is_parent:
   print("parent")
else:
   print("not man or perant")


# Comarision operators:
# Comparison operators are used to compare two values

is_grade = 7
if is_grade == 100:
   print("you got the full mark")
elif is_grade >= 50:
   print("well done")
elif is_grade < 50 and is_grade > 10 :
   print("you could make it better")
elif is_grade != 0:           # Not equal (!=)
   print("good job!")
else:
   print("you can do better next time")

print("exam done!")