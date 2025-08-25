# For loop

# for loop: used to repeat code or iterate through a sequence (list, range, etc.)
# for loop: prints whatever is inside the loop body
name = "how are you"
for item in name:
    print(item)


num = "habiba"
for item in range(1,10,2):
    print(item)


name = "hi"
for item in [1,2,3,4,5]:
    print(item)

# for loop to go through each character in the string
# condition: if the char is "o" (small or capital) → replace it with "0"
# using lower() makes the check case-insensitive
# build the result string step by step and print it at the end

msg = "good morning python learner"

res = ""

for x in msg:
    if x.lower() == "o":
        x = "0"
    res += x
print(res)