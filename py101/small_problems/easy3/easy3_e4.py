# strings strings
# write a function that takes one arg -> a positive int, and returns str of
# alternating 1s & 0s, always starting w/ a 1; len(str) should match given int

def stringy(str_len):
    return "".join(["1" if num % 2 == 0 else "0" for num in range(str_len)])

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True