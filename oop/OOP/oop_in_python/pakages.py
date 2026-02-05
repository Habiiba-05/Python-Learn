# Pakges

# import file_name:
# imports the whole module. To access anything inside it, i need to write
# file_name.func("value")

import name
print(name.fname("habiba"))


# from 'folder.file_name/file_name' import 'function' 
# imports the function directly, so I can just write
# func("value")

from name import fname
print(fname("habiba"))


# __init__
# is used so Python understands that the folder is a package.
#  It’s also useful if I want to control what gets exposed when someone does:
# from 'folder.file_name/file_name' import 'function'



# The difference between a package and a module is that 
# a package is a folder containing multiple Python files (and possibly an __init__.py), 
# while a module is just a single .py file.





## pypi and pip:
# it's 'python pakage index' Since it’s open-source, 
# I check which package I need, copy it, 
# then paste it in the terminal with pip before it. 
# If I want to make sure it’s actually installed, 
# I run pip list and it will show up.