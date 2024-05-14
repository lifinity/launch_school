# multiply by five
def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# number is a string; have to convert it to an int for n * 5 to return 50
# otherwise you just get string concat so an input of 10 * 5 = 1010101010