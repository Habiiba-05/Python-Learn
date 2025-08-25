# return statement

# Example 1: Function with no return statement

def greet(name):
    print(f'hello {name}')

# When I call the function, it prints the message
# BUT since there is no return statement, the function returns None by default
print(greet("habiba"))        # prints "hello habiba" and then prints "None"



# Example 2: Function with a return statement
def greet(name):
    return f'hi {name}'

# Here the function executes print inside,
# and because I returned it, the function itself returns the value of print (which is None)
print(greet("hanna"))       # prints "hi hanna", but does not print "None" 


# Example 3
def count(num):
    return num * num

print(count(2))