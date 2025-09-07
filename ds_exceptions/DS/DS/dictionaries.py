# Dictionaries

# Each element consists of a key and a value.
# Keys must be unique, but values can be repeated.
# Mutable → You can modify, add, or remove items.
# Unordered (maybe)
# No indexing by position → Unlike lists or tuples,
# you cannot access items by index; you access them using their keys.


# Dict: Unordered*, Mutable, Keys Unique, Access by Key


my_dict = {"name": "Alice", "age": 25, "city": "Cairo"}

# Access value by key
print(my_dict["name"])   
# output : Alice

# Add or modify
my_dict["age"] = 26
my_dict["job"] = "Engineer"
print(my_dict)           
# output : {'name': 'Alice', 'age': 26, 'city': 'Cairo', 'job': 'Engineer'}

# Check if a key exists
print("city" in my_dict) # True

# Iterate over keys and values
for key, value in my_dict.items():
    print(key, ":", value)
