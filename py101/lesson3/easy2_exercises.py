# q1; 2 distinct ways of reverse list w/o mutating original list
'''
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

numbers2 = [num for num in reversed(numbers)]
print(numbers2)
numbers3 = sorted(numbers, reverse=True)
print(numbers3)
numbers4 = numbers[::-1]
print(numbers4)
print(numbers)
'''
# solution used list(reversed(numbers)), cleaner than list comprehension

# q2; given a number & list, determine if # included in list
'''
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
print(f'is {number1} in {numbers}? {number1 in numbers}')
print(f'is {number2} in {numbers}? {number2 in numbers}')
'''

# q3; programmatically determine if 42 lies btwn 10 & 100 inclusive; ditto for 100 & 101
'''
print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))
'''
# originally did print(42 >= 10 and 42 <= 100); less pythonic, probably

# q4; given list of numbers, mutate by removing # at index 2
'''
numbers = [1, 2, 3, 4, 5]
print(f'before: {numbers}')
numbers.pop(2)
print(f'after: {numbers}')
'''
# solution used del numbers[2]; differs in that doesn't return a value

# q5; how to verify whether data structs assigned to given variables are of type list?
'''
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list)
print(type(table) is list)
'''
# isinstance(var_name, list) preferred b/c faster & considers inheritance

# q6; given a 40-chara wide table, how can we center a title above it?
'''
title = "Flintstone Family Members"

print(title.center(40))
print(f'{title:^40}')
'''

# q7; write a one-liner to count # of lowercase t charas in following strs
'''
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))
'''

# q8; determine if given dict of ppl & their ages contains an entry for 'Spot'
'''
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('Spot' in ages)
'''

# q9; given dict of family members & ages, add additional entries as provided
'''
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

print(f'before: {ages}')
ages.update(additional_ages)
print(f'after: {ages}')
'''