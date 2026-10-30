# login , if name is in admin?
# practical membership control 
'''admin = ['jk', 'habiba', 'becca', 'ran']
name = (input('whats youre name?'))

if name in admin:
   print(f'youre namr is {name} and youre an admin')
  
   option = input('you wanna delete or modify ur name?')

   if option == 'modify':
      newname= input('inter the new name:')
      print(f'the updated name is {newname}')

      admin[admin.index(name)] = newname

      print('name updated')
      print(admin)

   elif option == 'delete':
     admin.remove(name)
     print('name deleted')
     print(admin)
else:
   login = input('not an admin wanna be? yes? no?')

   if login == 'yes':
      print('youre with us')
      admin.append(name)
      print(admin)

   else:
      print('youre not added')'''




# loop
# password guess

'''tries = 3
password = "us"
inputpass = input('enter the pass: ')

while inputpass != password :
   tries -= 1
   print(f'wrong! try again there is {tries} left')
   inputpass = input('enter the pass: ')

   if tries == 0: 
      print('no chances left!')
      break
      
      print('bye bye!')

else:
   print('loop is done!')'''


# training book mark
import datetime

from cv2 import reduce


countries = ["Japan", "Korea", "Italy", "France"]

i = 0

while i < len(countries):
    print(countries[i])
    i += 1





# for loop

mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in mynumbers:

    if number % 2 == 0 :
        print(f'nummer {number} is even')
    else:
        print(f'nummer {number} is odd')

else:
    print('the end')


# another training

mycountry = {
    "japan" : "80$",
    "korea" : "90$",
    "china" : "50$",
}

for country in mycountry:
    print(mycountry['japan'])
    
    print(f'my {country} is: {mycountry[country]}')

# nasted loop

people = {
    'jk' : {
        'english' : '70' ,
        'music' : '100',
        'dance' : '100'
    },
    'RM' : {
        'english' : '100' ,
        'music' : '90' ,
        'dance' : '80'
    }
}

for name in people:
    print(f'hi {name} thats the score')
    for score in people[name]:
        print(f'- {score.upper()} => {people[name][score]}')


# pass, continue , break

numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number == 5:

      break
    print(number)


numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number == 5:

      pass
    print(number)


numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number == 5:

      continue
    print(number)


# loop advanced dictionary
langue = {
    'niney' : {
        'css' : '90',
        'js' : '80'
    } ,
     'sarah' : {
         'css' : '70' ,
         'js' : '90'
     }
}
for main_key, main_value in langue.items() :     # items() cause there is more then one value
    print(f'- {main_key} progress is: ')

    for child_key, child_value in main_value.items():
        print(f'- {child_key} => {child_value}')



# function

def full_name(first, middle, last):

    print(
          f"hello yall my name is {first.strip().capitalize()} {middle.strip():.1s} {last.strip().capitalize()}")

full_name("habiba", "jeon", "jeon")


# function packing and unpacking argument

def my_travel(name, *country):
    print(f'hello my name is {name} and i traveled to: ')

    for travel in country:
        print(travel)

my_travel('habiba', 'japan', 'US', 'korea', 'UK')


# function default parameter

def show_info(name, country ='unknown', age = 'unknown'):
    print(f'my name is {name} and i live in {country} and my age is {age}')

show_info('habiba', 'US, california', 25)
show_info('niney', 'US, nyc')
show_info('hanna', 'KSA', 25)


# func paking unoaking **arg its mainly used for dictionary'
def my_words(**dreams):
    print(type(dreams))

    for word, value in dreams.items():
        print(f'{word} => {value}')

my_words(ILETS ='8.0', KHS = 'accepted', stanford = 'accepted', flight = 'booked')


# function scope
x = 1 
def one():
    x = 7
    print(f"my favourite number is {x}")

def two():
    global x
    x = 3
    print(f"i have {x} exams")


print(f"the scope is number{x}")
one()
print(f"the scope is {x}")
two()
print(f"the scope is {x}")


# function recursion

def cleanword(word):

    if len(word) == 1:
        return word 

    if word [0] == word[1]:
        return cleanword(word[1:])

    return word[0] + cleanword(word[1:])

print(cleanword("wwwworlldddd"))


# lambda function
def worldwide(band, number):
    return f'they are {band} and they are {number}'

hello = lambda band, number: f"we're {band} and we're {number}"

print(worldwide("bantan", 'seven'))
print(hello("BTS", 7))


# file handaling
## read file
file = open('C:\ML journy\habi.txt', 'r')

print(file.read(5))

for line in file:
    print(line)

    if line.startswith('rm'):
        break

## writing and append

file = open(r'C:\ML journy\japan.txt', 'w')   # create the file
file.write("hi this is nabi\n")     # write the contant in the file
file.write("hope your doing well")

#list = ['im\n', 'in\n', 'japan finally\n', '2033']
#file = open(r'C:\ML journy\japan.txt', 'w') 
#file.writelines(list)

file = open(r'C:\ML journy\habi.txt', 'a') 
file.write("suga")

## important info
file = open(r'C:\ML journy\japan.txt', 'a')
file.truncate(5)

file = open(r'C:\ML journy\japan.txt', 'a')
print(file.tell())

file = open(r'C:\ML journy\japan.txt', 'r')
file.seek(5)
print(file.read())

#import os
#os.remove(r"C:\ML journy\japan.txt")


# built in func
a = [1, 2, 3, 4, 5]

if all(a):
    print("all is true")

else:
    print("at least one is false")

#
x = [0, 1, []]

if any(x):
    print("at least one in true")

else:
    print("all false")
#
print(bin(700))
#
a = 1
b = 2
print(id(a))
print(id(b))
#
mylist = [10, 7, 97, 13, 26]
print(sum(mylist, 5))  # add 5 on the list sum

#
a = 225.545
x = 225.554
print(round(a))
print(round(x, 2))

# 
print(list(range(0, 10, 2)))

# 
print("my","name","is","habiba", sep = "|")

print('-' * 50)

# abs
print(abs(100))
print(abs(-100))
print(abs(-10))
print(abs(10.07))

print('-' * 50)


# pow (base, exp, mode)
print(pow(2 , 3))
print(pow(2 , 3, 3))

print('-' * 50)

# min()
a = [1, 2, 3, 4, 5, -100, 50]
print(min(a))

print('-' * 50)

# max()
a = [1, 2, 3, 4, 5, -100, 50]
print(max(a))

print('-' * 50)

# slice (start, stop, step)
a = [1, 2, 3, 4, 5, -100, 50]
print(a[slice(0, 5, 2)])

print('-' * 50)

# use map with predefined function 
# if var
def formattext(text):
    return f"- {text} -"
mytext = ['habi', 'travel', 'the world']
myformateddata = map(formattext, mytext)
print(myformateddata)
# if loop
mytext = ['habi', 'travel', 'the world']
for name in myformateddata:
    print(name)

print('-' * 50)

# if lambda
mytext = ['habi', 'travel', 'the world']
for name in list(map(lambda text: f"- {text} -" , mytext)):
    print(name)

print('-' * 50)

# filter
#ex1
def countries(travel):

    if travel == "japan":
      return travel  

mycountries = ['japan', 'US', 'korea']
myresults = filter(countries, mycountries)

for counrtyy in myresults:
    print(counrtyy)

# ex2
def mynumbers(num):

    if num < 50:
        return num

thenums = [1, 2, 3, 4, 5, 6, 7, 100, -100]
theresult = filter(mynumbers, thenums)
for number in theresult:
    print(number)

#ex3 \ using lambda
mypeople = ["habiba", "bts", "hana", "ys people"]
for name in filter(lambda name: name.startswith("b"), mypeople):
    print(name)

print('-' * 50)

from functools import reduce
def sumall(num1, num2):
    return num1 + num2
numberr = [1, 2, 3, 7, 50]

mysumation = reduce(sumall, numberr)
print(mysumation)

# using lumbda
mysumation = reduce(lambda num1, num2: num1 + num2, numberr)
print(mysumation)

print('-' * 50)

# enumerate
myskill = ['css', 'html', 'py']
myskilwithcounter = enumerate(myskill, 7)
for c, l in myskilwithcounter:
    print(f"{c} - {l}")

print('-' * 50)

# help - to know info abt smth
# print(help(print))

print('-' * 50)

# reverse
myskill = ['css', 'html', 'py']

myskilwithcounterr = reversed(myskill)
for skill in myskilwithcounterr:
    print(skill)

print('-' * 50)

# create your module 

# to add another path
#import sys
#sys.path.append(r"D:\travel")
#print(sys.path)

# import habi
import ifb
ifb.iwannatravel("Stanford (CA, US)")
ifb.sayhello("sakura")

from ifb import iwannatravel as iwt
iwt("japan")

print('-' * 50)

# date and time 
print(datetime.datetime.now())

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

print(datetime.datetime.min)
print(datetime.datetime.max)

print(datetime.datetime.now().time())

print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)

print(datetime.time.min)
print(datetime.time.max)

print(datetime.datetime(2005, 1, 1, 12, 7, 3, 45926))

mybd = datetime.datetime(2005, 1, 1)
date = datetime.datetime.now()
print(f"my BD: {mybd}")
print(f"and now is: {date}")

# complete the last one 

print('-' * 50)

# format the date
# str is convert the numbers to string and %a => the short. %A => the whole thing
import datetime
mybd = datetime.datetime(2005, 1, 1)
print(mybd.strftime( "%a" ))
print(mybd.strftime( "%A" ))
print(mybd.strftime( "%b" ))
print(mybd.strftime( "%B" ))

print('-' * 50)

# iterable vs iterator

# start with iterable 
mystring = "habiba"
for letter in mystring:
    print(letter, end=" ") 

mylist = [2005, 97, 13, 7]
for number in mylist:
    print(number, end=" ")

# iterator
mypeople = ("hana", "jk", "sarah", "niney", "faridas")
for person in iter(mypeople):
    print(person, end=" ")

print('-' * 50)

# generator

def mygenerator():

        yield 1
        yield 2
        yield 3
        yield 4

mygen = mygenerator()

for gen in mygen:
    print(gen)

print('-' * 50)

# decorator
def mydecorator(func):

    def nestedfunc():
        print("before")
        func()
        print("after")

    return nestedfunc

@mydecorator
def sayhello():
    print("hii")

@mydecorator
def saywhoru():
    print("hello")

sayhello()
saywhoru()

print('-' * 50)

# decorator(func and parameter)

def mydecorator(func):

    def nestedfunc(a, b):
        if a < 0 or b < 0:  
          print("one of nums are less than zero")
        func(a, b)
        

    return nestedfunc

@mydecorator
def calculate(a, b):
    print(a + b)

calculate(-7, 13)
print('.' * 50)
calculate(7, 13)

print('-' * 50)

# decorator(Practical Speed Test)
def mydecorator(func):

    def nestedfunc(*numbers):
        for number in numbers:
          if number < 0:  
            print("one of nums are less than zero")
        func(*numbers)
        

    return nestedfunc

@mydecorator
def calculate(a, b, c):
    print(a + b + c)

calculate(-7, 13, 100)

print('-' * 50)

# SpeedTest
def speedtest (func):
    def wrapper():
        start = datetime.time()
        func()
        end = datetime.time()
        print(f"func running time is {end - start} ")
        return wrapper

def bigloop():
    for number in range(1, 4000):
        print(number)

bigloop()


print('-' * 50)


# zip()

# 1
list1 = [1, 2, 3, 4]
tuple2 = ("a", "b", "c")
combain = zip(list1, tuple2)
print(list(combain))


print('-' * 50)


# 2
list1 = [1, 2, 3, 4]
list2 = [13, 97, 29, 7]
tuple2 = ("a", "b", "c")
dict1 = {"name": "habiba", "age": 21}
for item1 , item2, item3 , item4  in zip(list1, list2, tuple2, dict1):
    print("for list1 item is =>", item1)
    print("for list2 item is =>", item2)
    print("for tuple2 item is =>", item3)
    print("for dict1 item key =>", item4, "|", "value =>", dict1[item4])


print('-' * 50)


# pillow library - image manipulation

# 1 - show
# from PIL import Image
# myimage = Image.open(r"C:\ML journy\python_learn\Untitled design.png")
# myimage.show()


print('-' * 50)


# 2 - crop it
# from PIL import Image
# myimage = Image.open(r"C:\ML journy\python_learn\Untitled design.png")
# mybox = (50, 50, 200, 200)
# newimage = myimage.crop(mybox)
# newimage.show()


print('-' * 50)


# 3 - convert
# from PIL import Image
# myimage = Image.open(r"C:\ML journy\python_learn\Untitled design.png")
# myconvert = myimage.convert("L")
# myconvert.show()


print('-' * 50)


# commenting and documenting | doc string
def myfunc(name):
    """
    documenting
    what the code func
    did
    """
    print(f"my name is {name}")

myfunc("habiba")

print(myfunc.__doc__)
help(myfunc)


print('-' * 50)


# error and exeptions 
# x = -10
# if x < 0:
#    raise Exception(f"its {x} so its less than zero")
#    print("will not print")
# else: 
#    print("its greater than zero")

# print('-' * 50)

# y = "jk"

# if type(y) != int:
#    raise ValueError("only nums")

# print('print msg after condition')


print('-' * 50)


# exeption handaling try\except\else\finally
try:
    print(x)
    print(10 / 0)
    print(int("habi"))

except NameError:
    print("x not with us")

except ZeroDivisionError:
    print("wrong math")

else:
    print("not included")

finally:
    print("not assigned")


print('-' * 50)


# debuging
mylist = [1, 2, 3, 4, 5]
mydict = {"name": "habiba", "age":21}

for num in mylist:
    print(num)

for key, value in mydict.items():
    print(f"{key} => {value}")

def func_one():
    print("hello")

func_one()


print('-' * 50)


# type hinting
def calculate(a, b) -> int:
    print(a + b)
calculate(7, 13)

def myname(name) -> str:
    print(f"hello {name}")
myname("bangtan")