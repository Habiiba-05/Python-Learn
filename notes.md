# Python Notes

## 1. Check Python Version
```python
import sys
print(sys.version)
```

---

## 2. Do Not Name Files After Libraries
Avoid naming any code file the same as a Python library — this will cause an error.

---

## 3. Comment/Uncomment Shortcut
Use:
- **Windows:** `Ctrl + /`
- **Mac:** `Command + /`
This will toggle the code between comment and uncomment.

---

## 4. Triple Double Quotes
`""" bla bla bla """` are multi-line strings, **not comments**.

---

## 5. Common Data Types
```python
# int - integer numbers
print(type(10))

# float - floating point number
print(type(100.99))

# str - string
print(type("hello"))

# bool - boolean (True/False)
print(type(2 == 2))  # True
print(type(2 == 4))  # False
```
When using `type()`, the output will be the **variable’s type**, not its value.

---

## 6. If Statement & Indentation
Python requires indentation after `if` statements, otherwise it will throw an error.
```python
if 1 < 8:
    print("one is less than eight")
```

---

## 7. Variable Naming Rules
- Can start with `(a-z, A-Z)` or underscore `_`.
- Cannot start with numbers or special characters.
- Can include numbers `(0-9)` or underscore `_`.
- Variable names are case-sensitive: `age`, `Age`, and `AGE` are different variables.

**Naming styles:**
- `name` → normal
- `myName` → camelCase
- `my_name` → snake_case

**Example:**
```python
name = 10
print(name)
```

---

## 8. Dynamic Typing
Python is dynamically typed — the last assigned value to a variable is what gets printed.
```python
x = 10
x = "hi"
print(x)  # Output: hi
```

---

## 9. Reserved Keywords
Use:
```python
help("keywords")
```
This displays Python’s reserved words — you cannot use them as variable names.

---

## 10. Numbers
Numbers can be written directly without declaring type:
```python
age = 20      # Preferred
age = int(20) # Works, but less clean
```
When printing numbers with text, convert to string:
```python
age = 20
print("My age is " + str(age))
```

---

## 11. String Concatenation
When using `+`, make sure to add spaces if needed:
```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # Output: Python is awesome
```

---

## 12. Global Variables
A global variable can be accessed anywhere in the program.  
Example:
```python
name = "John"  # Global

def print_name():
    print(name)

print_name()  # Output: John
```

---

## 13. `global` Keyword
### Case 1: Make a local variable global
If a variable is created inside a function but you want it to be global, use `global`:
```python
def set_global():
    global name
    name = "John"

set_global()
print(name)  # Output: John
```

### Case 2: Modify an existing global variable inside a function     
```python
x = "Hello"

def change_global():
    global x
    x = "Hi"

change_global()
print(x)  # Output: Hi
```
