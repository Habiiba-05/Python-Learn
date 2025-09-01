# Class student lab

# first way
from name import my_name
print(my_name("habiba"))

from name import age
print(age(20))




# second way

class student():

    def name(self):
        pass
    def age(self):
        pass

class name1(student):
    def name(self):
        print("the student name is habiba, ")

class age1(student):
    def age(self):
        print("and her age is 20. ")

my_name = name1()
my_age = age1()

my_name.name()
my_age.age()



# Third way 
class student():

    def __init__(self, name, age):
        self.name = name
        self.age = age 

student = student("habiba", 20)
print(f'the student name is {student.name}, and her age is {student.age}')