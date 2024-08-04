# convert a number to a string
# write a function that converts a non-negative int to a string
# representation of that int; standard conversion funcs not allowed

# input: int
# output: str

# explicit rules
# - input int will be non-negative (don't worry about sign)
# - standard conversion functions like str() aren't allowed

# implicit rules
# - 0 counts as a non-negative number and is valid input
# - number % 10 gets you the rightmost number
# - number // 10 truncates away the rightmost number

# questions (theoretical)
# - max input/output length?
# - possible to have invalid/non-numerical input? (assumed no)
# - !! leading zeroes in input? turns out impossible! syntax error.

# data structures
# dict for int digit -> string conversion
# !! better opt is to use a list directly b/c the indices act as keys
# !! can also use a string literal directly '0123456789' b/c indexable

# algorithm
# 1. define a conversion mapping for single-digit int to a str
# 2. isolate single nums from input and convert & add to output str
# 3. return output str once no more numbers to process

# note; python has a built-in divmod(a, b) -> (a // b, a % b)

NUMBERS = [str(num) for num in range(10)]

def integer_to_string(num):
    result_str = ''
    while num > 0:
        num, rightmost_num = divmod(num, 10)
        result_str = NUMBERS[rightmost_num] + result_str
    return result_str or NUMBERS[num] # '0' edgecase

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True