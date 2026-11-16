count = 1
total = 0

# BUG: The while line was missing a colon at the end (SyntaxError). Added the ':'.
# BUG: Used < so the loop stopped before adding 5 (result was 10, not 15). Changed to <= so 5 is included.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Can't join a string and an int with + (TypeError). Wrapped total in str() to convert it to text.
print("Sum of 1 to 5 is: " + str(total))