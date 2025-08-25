# Loops
# You must have a condition to break out of the loop, otherwise it will keep running forever


# While loop
counter = 2
while counter <= 10:
    print(counter)
    counter += 1

# simple guess-the-number game:
# user has only 2 attempts to guess the correct number
# if the guess is correct → print message and break out of the loop
# if the guess is wrong → print "try again" until attempts are used up

num = 10
count = 0    
while count < 2:
    guess_num = int(input("please guess the number"))
    count += 1
    if num == guess_num:
        print("you are correct") 
        break
    else:
        print("try again")