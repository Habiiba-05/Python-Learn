# exception handling

# it's block - Place in the code to handle errors that may occur

a = 5
try:
    print(t)
except:
    print("an axception accurred")


a = 5
try:
    print(a)
except:
    print("an axception accurred")


try:
    print(y)
except NameError:
    print("variable y is not define")
except:
    print("somthing else went wrong")


try:
    print(i)
except:
    print("somthing went wrong")
else:
    print("nothing went wrong")

try:
    print(z)
except:
    print("somthing went wrong")
finally:
    print("the try'except1' is finished")