# numpy

# multidimentional array

# 1 - multiply elements by 2
import numpy as np
from numpy import array

mylist = np.array([1, 2, 3, 4])
mylist = mylist * 2
print(mylist)


print("-" * 50)


# 2 - multidimentional array

# zero dimentional
import numpy as np
array1 = np.array("a")
print(array1.ndim)

print("-" * 50)

# one dimentional
import numpy as np
array1 = np.array(["a" , "b"])
print(array1.ndim)

print("-" * 50)

# two dimentional
import numpy as np
array1 = np.array([["a", "b", "c"], ["d" , "e", "f"]])
print(array1.ndim)

print("-" * 50)

# three dimentional
import numpy as np
array1 = np.array([[["a", "b", "c"]], 
                   [["d" , "e", "f"]],
                   [["g" , "h", "i"]]])
print(array1.ndim)
print(array1.shape)

print("-" * 50)

# create the word "japan"
import numpy as np
array1 = np.array([[["a", "b", "c"], ["d" , "e", "f"], ["g" , "h", "i"]], 
                   [["j", "k", "l"], ["m" , "n", "o"], ["p" , "q", "r"]],
                   [["s", "t", "u"], ["v" , "w", "x"], ["y" , "z", " "]]])

japan = array1[1, 0, 0] + array1[0, 0, 0] + array1[1, 2, 0] + array1[0, 0, 0] + array1[1, 1, 1]
print(japan)


print("-" * 50)


# slicing(start:end:step)
myarray = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9],
                   [10, 11, 12]])

# 1- rows
print(myarray[0:3:2])
print("-" * 50)

print(myarray[-1:])
print("-" * 50)

# 2- columns
print(myarray[:, 1])
print("-" * 50)

print(myarray[:, -1])
print("-" * 50)

print(myarray[:, 0:2])
print("-" * 50)

print(myarray[:, ::2])
print("-" * 50)

print(myarray[:, 1::3])
print("-" * 50)

# 3- row and column
print(myarray[1:3, 0:2])



print("-" * 50)



# arithmetic

# 1 - scalar arithmetic
a = np.array([1, 2, 3])
print(a * 2)
print(a - 3)
print(a ** 2)
print(a / 2)
print(a % 2)


print("-" * 50)


# 2 - vectorized math func 
c = np.array([1.05, 2.5, 3.7])
print(np.round(c))
print(np.floor(c))
print(np.ceil(c))
print(np.sqrt(c))


print("-" * 50)


# 3 - element-wise arithmetic 
b = np.array([7, 6, 5])
t = np.array([1, 2, 3])
print(b + t)
print(b - t)
print(b ** t)
print(b / t)
print(b % t)


print("-" * 50)


# 4 - comarison operators
j = np.array([13, 7, 97, 100, 21, 93])
print(j < 50)
print(j >= 50)
j [j > 50] = 0
print(j)


print("-" * 50)


# broadcasting

# 1
array1 = np.array([13, 7, 97, 100, 21])
array2 = np.array([[1],[2],[3],[4],[5]])
print(array1.shape)
print(array2.shape)
print(array1 * array2)


print("-" * 50)


# aggregate function
array3 = np.array([[10, 11, 12, 13],
                   [1, 2, 3, 4]])

print(sum(array3))
print(np.sum(array3, axis=0))
print(np.sum(array3, axis=1))


print("-" * 50)


# filtiring
# 1
ages = np.array([[22, 18, 60, 19, 100],
                 [20, 21, 25, 30, 15]])

students = ages[ages < 25]
adults = ages[ages >= 25]
people = ages[(ages >= 25) & (ages < 100)]
print(students)
print(adults)
print(people)

print("-" * 50)

# 2 - where()
ages = np.array([[22, 18, 60, 19, 100],
                 [20, 21, 25, 30, 15]])
adults = np.where(ages >= 25, ages, 0)
print(adults)


print("-" * 50)


# random number 
# 1 
import numpy as np
a = np.random.default_rng()
print(a.integers(1, 10))

# 2 
import numpy as np
a = np.random.default_rng(seed=1)
print(a.integers(low=1, high=100, size=(3, 3)))

# 3 
np.random.seed(seed=1)
print(np.random.uniform(low=1, high=5, size=3))

# 4
yall = np.random.default_rng()
yall2 = np.array([1, 2, 3, 4])
yall.shuffle(yall2)
print(yall2)

# 5 
yall = np.random.default_rng()
members = np.array(["jk", "v", "rm", "d"])
member = yall.choice(members, size=(3, 2))
print(member)