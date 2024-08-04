# convert string to signed number
# write a function that takes a string of digits & returns appropriate
# number as integer; string may have leading + or - sign and should
# return a positive & negative num respectively; if no sign, positive
# may assume str will always contain a valid number; standard conversion
# func not allowed; can reuse string_to_integer from prev exercise (easy1_e8)

# input: str
# output: int

# explicit rules
# - return positive int if no sign or + sign
# - return negative int if leading - sign
# - input string will always have valid number (no weird chars or empty str)
# - standard conversion functions like int() not allowed but can reuse
# previously written string_to_integer()

# implicit rules 
# - if they exist, +/- will always be the first character in the input str
# - empty string invalid input; will always h

# questions (theoretical; same as prev)
# - max str/number length?

# data structures
# dict for str to int conversion (as per prev)

# algorithm
# check beginning of string for sign & save in variable
# convert rest of string (excluding sign) into an int (using string_to_integer)
# adjust the converted int to have the correct sign & return

NUMBERS = {str(num) : num for num in range(10)}

def string_to_integer(num_str):
    return sum([NUMBERS[num_chr] * 10**idx for idx, num_chr
                in enumerate(num_str[::-1])])

def string_to_signed_integer(num_str):
    sign = -1 if num_str[0] == '-' else 1
    return sign * string_to_integer(num_str.strip('+-'))

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
print('-' * 10)
print(string_to_signed_integer("-014180") == -14180)   # True
print(string_to_signed_integer("+00238") == 238)       # True
print(string_to_signed_integer("0248003") == 248003)   # True