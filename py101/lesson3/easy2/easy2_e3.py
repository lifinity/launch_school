# q3; programmatically determine if 42 lies btwn 10 & 100 inclusive; ditto for 100 & 101
print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

# originally did print(42 >= 10 and 42 <= 100); less pythonic, probably