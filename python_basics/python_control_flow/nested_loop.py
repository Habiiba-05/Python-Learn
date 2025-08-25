# Nested loop

# nested loop = two for loops inside each other
# num1 is the counter of the outer loop, num2 is the counter of the inner loop
# outer loop stays fixed until the inner loop finishes all its iterations
# here: both loops run over range(2) → possible values are 0 and 1
# inner loop runs fully for each value of the outer loop
# result: prints all combinations of (num1, num2) → (0,0), (0,1), (1,0), (1,1)

for num1 in range(2):
    for num2 in range(2):
        print(f'{num1},{num2}')

