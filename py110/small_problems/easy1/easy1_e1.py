# searching 101
# write a program that solicits 6 numbers from user & prints msg that describes
# if 6th number appears among the first 5

# input: user input; int (assumed)
# output: console output; string

# explicit rules:
# - ask for user input 6 times
# - output message needs to say whether 6th # provided as one of the previous 5 inputs

# implicit rules:
# - user input should be a number, presumably an int based on examples
# - need exactly 6 valid user inputs; keep asking until obtained

# questions (theoretical)
# - only ints or any number, e.g. floats, etc, allowed?
# - expected behavior when no/invalid input? keep asking?

# data structure:
# list for storing user input; necessary for determining if 6th input among them later

# algorithm:
# 1. repeatedly ask user to input a number until you have enough valid numbers (6)
# 2. check if 6th number same as any of the previous numbers
# 3. print msg confirming/denyingaccordingly

# reused from py101 easy3_e10
def num_suffix(num):
    last_digit = num % 10
    penult_digit = (num // 10) % 10

    if penult_digit == 1:
        return 'th'
    
    match last_digit:
        case 1: return 'st'
        case 2: return 'nd'
        case 3: return 'rd'
        case _: return 'th'

NUM_INPUTS = 6

def valid_num(num):
    try:
        int(num)
    except ValueError:
        return False
    return True

def searching_101():
    input_nums = []

    for i in range(1, NUM_INPUTS+1):
        get_num = input(f"Enter the {i}{num_suffix(i)} number: ").replace(',', '')
        while not valid_num(get_num):
            print("Invalid input. Numbers only please.")
            get_num = input(f"Enter the {i}{num_suffix(i)} number: ").replace(',', '')
        input_nums.append(get_num)
    
    nums_except_last = input_nums[:-1]
    is_in_str = "is in" if input_nums[-1] in nums_except_last else "isn't in"
    print(f"{input_nums[-1]} {is_in_str} {','.join(nums_except_last)}.")

searching_101()

# further exploration: does this still work if problem changed to look for a num that 
# satisfies a condition (e.g. num > 25) instead of if a specific number exists in a subset? 
# why or why not?

# current solution wouldn't work as-is b/c 'in' only checks presence of number & can't do
# criteria passing check but to modify: after getting input, list comprehension or loop to 
# get num(s) that satisfy condition