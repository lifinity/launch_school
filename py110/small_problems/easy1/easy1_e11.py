# convert signed number to string
# write function that takes int & converts to string representation
# but also accounts for negative numbers; can't use standard conversion
# functions but integer_to_string from prev exercise (easy1_e10) allowed

# input: int
# output: str

# explicit rules
# - input can be 0, positive or negative
# - standard conversion functions like str() aren't allowed but
# can reuse previously written integer_to_string

# implicit rules
# - first letter of output should indicate sign
# - 0 doesn't have a sign

# questions (theoretical)
# - max input/output limitations?
# - possible to have invalid/non-numerical input? (assumed no)

# data structures
# list as required by integer_to_string for conversion

# algorithm
# 1. figure out sign necessary prepend to output str
# 2. convert the unsigned (absolute) value of the number
# 3. prepend sign as necessary and return output str

NUMBERS = [str(num) for num in range(10)]

def integer_to_string(num):
    result_str = ''
    while num > 0:
        num, rightmost_num = divmod(num, 10)
        result_str = NUMBERS[rightmost_num] + result_str
    return result_str or NUMBERS[num] # '0' edgecase

def signed_integer_to_string(num):
    sign = '+' if num > 0 else '-'
    converted_str = integer_to_string(abs(num))
    return sign + converted_str if num else converted_str

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True