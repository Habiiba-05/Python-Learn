msg = "good morning python learner"

res = ' '

for x in msg:
    if x.lower() == "o":
        x = "0"
    res += x

print(res)



