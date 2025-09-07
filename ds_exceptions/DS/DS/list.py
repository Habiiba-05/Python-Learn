# Lists

# List Methods:

# Append(item) - Adds an element to the end of the list
# Insert(pos, item) - Adds an element at the position pos
# Extend(another_list) - Concatenate another_list/any other sequence to the end
# Remove(item) - Removes the item from a list
# Pop(pos) - Removes the item at the position pos. If no pos, removes last
# Clear() - Delete items from the list, but the list itself is still there

# indexing and slicing like strings

# Concatenate - Merge of the same type, for ex:
# my_list = my_list + ["habiba"]

# len()  -   returns the number of items in the object

# my_list*2   -   repeat the list again 



numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
print(type(numbers))
# output : list

numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
print(numbers*2)
# output : [1, 2, 3, 4, 5, 100.2, 'habiba', 1, 2, 3, 4, 5, 100.2, 'habiba']

numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
print(len(numbers))
# output : 7

numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
numbers += ["mohamed"]
print(numbers)
# output : [1, 2, 3, 4, 5, 100.2, 'habiba', 'mohamed']
# don't forget [] when you add new item to the list

numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
numbers.append(20)
print(numbers)
# output : [1, 2, 3, 4, 5, 100.2, 'habiba', 20]

numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
print(numbers[1:6])
# output : [2, 3, 4, 5, 100.2]
# last index doesn't count

numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
print(numbers[6][-3])
# output : i

numbers = [1, 2, 3, 4, 5, 100.2, "habiba"]
print(numbers[:3])