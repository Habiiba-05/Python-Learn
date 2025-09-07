# Tuples



# Define a tuple (use parentheses ())
# The difference between a list and a tuple is that a list can be modified,
#  while a tuple cannot be modified unless 
# you convert it to a list first and then turn it back into a tuple.



my_tuple = (1, "apple", 3.5, 1)
print(my_tuple)        
# output : (1, 'apple', 3.5, 1)

my_tuple = (1, "apple", 3.5, 1)
print(type(my_tuple))  
# output 'tuple'

my_tuple = (1, "apple", 3.5, 1)
print(my_tuple[0])   
# output : 1
my_tuple = (1, "apple", 3.5, 1)
print(my_tuple[1])  
# output: apple

my_tuple = (1, "apple", 3.5, 1)
print(len(my_tuple))  
# output : 4

my_tuple = (1, "apple", 3.5, 1)
print(my_tuple[1:3])  
# output : ("apple", 3.5)

my_tuple = (1, "apple", 3.5, 1)
print(my_tuple.count(1))       
# output : 2   
# count()  -  count how many times the item shows

my_tuple = (1, "apple", 3.5, 1)
print(my_tuple.index("apple")) 
# output : 1   