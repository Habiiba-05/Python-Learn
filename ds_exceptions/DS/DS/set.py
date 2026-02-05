# Set

# Unordered   -  elements do not have a fixed order 
# No duplicates  -  duplicate elements are automatically removed
# Mutable  -   you can add or remove elements
# No indexing or slicing  -  cannot access elements by position
# Useful for uniqueness and fast membership testing
# sort data from bottom to top



# Sets Methods:

# Accessing Set elements use: IN operator.
# You can add items using add()
# Same as extend() in lists, you can use update() to add two sets/any other sequence.
# Remove(): to remove and item from the set.
# Union() == Update(), but union() returns a new set. Update() modifies.
# Intersection(): get the duplicated items from two sets and return a new set.
# Intersection_update(): same as intersection(), but updates directly.


# Set: Unordered, Mutable, No Duplicates, No Index Access


my_set = {1, 2, 2, 3, 4}
print(my_set)  
# output : {1, 2, 3, 4}  duplicates removed

my_set = {1, 2, 2, 3, 4}
my_set.add(5)
print(my_set)  
# output : {1, 2, 3, 4, 5}

my_set = {1, 2, 2, 3, 4}
my_set.remove(3)
print(my_set)  
# output : {1, 2, 4, 5}

my_set = {1, 2, 2, 3, 4}
print(2 in my_set)   # True
print(3 in my_set)   # False

# 5- No indexing → this would cause an error:
# print(my_set[0])    # TypeError

my_set = {2, 5, 1, 2}
for item in my_set:
    print(item)       # prints elements in arbitrary order
# output : {1, 2, 5}