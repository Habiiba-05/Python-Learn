# Strings notes
# Strings in Python can be written in different ways:

# Single quotes
name = 'hello!'
print(name)

# Double quotes
book = "i read 'secrets of the millionaire mind' "
print(book)

# Triple quotes 
series = '''
my favorite series

is

friends
'''
print(series)

# Formatted strings

# Without it
# Output will be stuck together (no spaces)
first_name = "habiba"
last_name = "mohamed"
message = "my first name is " + first_name + "my last name is " + last_name
print(message)

# With it
# The output will look good
first_name = "habiba"
last_name = "mohamed"
msg = f'my first name is {first_name} and my last name is {last_name}'
print(msg)

# String methods
# 'len()' returns the number of characters in the string
name = "habiba"
print(len(name))

# return a specific character on specific index
# [] includes num of index inside
text = "i love reading"
print(text[2]) 

# Take char from the 'start index' until the end of the string
text = "i love reading"
print(text[0:])

# Take char from the 'start index' up to end 'index' (the part we selected)
text = "i love reading"
print(text[2:5])

# Using (-index) count from the end
text = "i love reading"
print(text[6:-1])

# Typing "name." show available strings method we can use
name = "habiba mohamed"
print(name.replace("ython", "air"))