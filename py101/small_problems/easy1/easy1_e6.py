# sum or product of consecutive integers
# write a program that asks user to enter int > 0, then asks if user wants 
# to determine sum or product of all numbers btwn 1 & the entered int, inclusive

def valid_number(num):
    try:
        if int(num) <= 0:
            raise ValueError
    except ValueError:
        return False
    return True

def get_int(prompt):
    int_input = input(prompt)

    while not valid_number(int_input):
        print("That's not an integer > 0. Try again.")
        int_input = input(prompt)
    
    return int(int_input)

def sum_or_product():
    range_end_int = get_int("Please enter an integer greater than 0: ")
    operation_type = input("Enter 's' to compute the sum, or 'p' to compute the product: ")

    match operation_type:
        case 's' | 'sum':
            total_sum = sum(range(1, range_end_int+1))
            print(f"The sum of all integers between 1 and {range_end_int} is {total_sum}.")
        case 'p' | 'product':
            total_product = 1
            for num in range(1, range_end_int+1):
                total_product *= num
            print(f"The product of all integers between 1 and {range_end_int} is {total_product}.")
        case _:
            print("Invalid operation chosen. Nothing computed.")

sum_or_product()

# further exploration: suppose input was list of space separated integers instead
# of a single int, how would your sum/product computations change?

# basic sum/product calculations wouldn't change assuming we need to find sum/product
# of range(1, int) for each int in the list, in which case we'd str.split() and
# iterate, running calcs & storing results in another list. another function would be
# needed to reduce into a single sum/product tho if that's the expected result