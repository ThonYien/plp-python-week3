count = 1
total = 0

# BUG: The while statement was missing a colon at the end.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The integer total cannot be joined to a string using +, so I used an f-string.
print(f"Sum of 1 to 5 is: {total}")