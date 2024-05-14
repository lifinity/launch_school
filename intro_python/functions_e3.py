# not named multiply.py
def multiply(a, b):
    return a * b

first_num = float(input('Enter the first number: '))
second_num = float(input('Enter the second number: '))
product = multiply(first_num, second_num)

print(f'{first_num} * {second_num} = {product}')

'''
# optionally modularize getting prompt too
def get_number(prompt):
  entry = input(prompt)
  return float(entry)
'''