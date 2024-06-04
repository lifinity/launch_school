def multiply(left, right):          # multiply, left, right
    return left * right             # left, right

def get_num(prompt):                # get_num, prompt
    return float(input(prompt))     # float, input, prompt

first_number = get_num('Enter the first number: ')        # first_number, get_num
second_number = get_num('Enter the second number: ')      # second_number, get_num
product = multiply(first_number, second_number)           # product, multiply, first_number, second_number
print(f'{first_number} * {second_number} = {product}')    # print, first_number, second_number, product