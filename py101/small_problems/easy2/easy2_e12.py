# always return negative
# write function that takes number as arg. if arg positive,
# return negative; if arg negative, return as-is

def negative(num):
    return num if num < 0 else num * -1

# official solution uses -abs(num), which.. yeah.

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True