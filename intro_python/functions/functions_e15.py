def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply: global
# left: local
# right: local

# get_num: global
# prompt: local
# float: built-in
# input: built-in

# first_number = global
# second_number = global
# product = global
# print = built-in