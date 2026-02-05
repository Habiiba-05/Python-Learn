# file handling


# File handling in Python has three main modes:
# 1. "r" (read): open file for reading only. If the file does not exist, it raises an error.
# 2. "w" (write): open file for writing. If the file already exists, it will be overwritten.
# 3. "a" (append): open file for adding new content at the end without deleting the old content.
#
# If the file is in the same folder as the script, just write its name.
# If it is not in the same folder, you must provide the full path.



# Reading:
# - read() will print the whole content at once.

f = open("exception\exception&file_handling\file_read.txt" , "r")
print(f.read())
f.close() 

# - reading line by line is safer for large files and allows you to control output.

f = open("file_read.txt", "r")
all_lines = f.readline()

for line in all_lines:
    print(line)


# Writing:
# - "w" mode will overwrite everything in the file unless you add "\n" for new lines.
# If the file does not exist, it is created

f = open("file_read", "w")
f.write("hello")
f.close()

f = open("file_read", "r")
f.write("hello")
f.close()


# Appending:
# - "a" mode adds content at the end of the file without removing old data.

f = open("file_read", "a")
for i in range(30):
    f.write("/nI love pytho" + str(i))

f.close()

f = open("file_read", "r")
f.write("hello")
f.close()


# Important:
# Always use "with open(...)" so the file closes automatically.
