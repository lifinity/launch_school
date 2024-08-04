# convert a string to a number
# write a function that takes a str of digits & returns appropriate
# number as int w/o using any standard conversion functions like int()
# function should calc result using characters in the string & for now,
# don't worry about + or - or invalid chars, assume all chars numeric

# input: str
# output: int

# explicit
# - can't use standard conversion functions like int()
# - need to calculate result using individual numbers
# - ignore positive/negative signs and assume all character numeric

# implicit
# - need to put each number in correct 'place', i.e. ones, tens; 
# each place increments by *= 10 (can use idx; 10^0 = 1, 10^1 = 10, etc)

# questions (theoretical)
# - max string/num length?
# - empty string valid input & what should it return if yes? (assume invalid)
# - possible to have leading zeros? (assumed no; tbh handled even if yes tho)

# data structures
# dict for storing single-digit number str to int conversion info
# alt; list for storing each place-adjusted digit of number string

# algorithm
# 1. define a way to convert any given number character to an int
# 2. for every number, convert and add to correct 'place' in result int
# 3. return finished int when no more numbers to add from string

# alt algorithm
# 1. define a way to convert any given number character into an int
# 2. for each num char, convert to int and multiply it by its place and save 
# 3. return the sum of all the place-adjusted digits to get the final int

NUMBERS = {str(num) : num for num in range(10)}

def string_to_integer(num_str):
    result_int = 0
    for num_chr in num_str:
        result_int = (result_int * 10) + NUMBERS[num_chr]
        print(result_int)
    return result_int

print(string_to_integer("4321") == 4321)    # True
print(string_to_integer("570") == 570)      # True

print('-' * 10)

print(string_to_integer("7000") == 7000)    # True
print(string_to_integer("60101") == 60101)  # True
print(string_to_integer("5") == 5)          # True
print(string_to_integer("00410") == 410)     # True

print('-' * 10)

# further exploration: write a hexadecimal_to_integer function that converts
# a string representing a hex number to its integer value; hexadecimal numbers
# use base-16 instead of 10, and characters: A, B, C, D, E, F (case insensitive)
# correspond to decimal vals 10 thru 15

# similar breakdown as string_to_integer just need to change base multiplication
# for each place (16 instead of 10) + more keys to account for extra hexa vals
# used an alt implementation that also works for og problem if 10**idx instead

HEX_NUMBERS = NUMBERS | {chr(ord('a') + idx) : num for idx, num in enumerate(range(10,16))}

def hexadecimal_to_integer(hex_str):
    return sum([HEX_NUMBERS[num_chr] * 16**idx for idx, num_chr
                in enumerate(hex_str.casefold()[::-1])])

print(hexadecimal_to_integer('4D9f') == 19871)  # True