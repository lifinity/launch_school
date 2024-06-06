# q4; given list of numbers, mutate by removing # at index 2
numbers = [1, 2, 3, 4, 5]
print(f'before: {numbers}')
numbers.pop(2)
print(f'after: {numbers}')

# solution used del numbers[2]; differs in that doesn't return a value
