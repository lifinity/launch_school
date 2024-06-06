# q1; 2 diff ways to remove all elements from given list
numbers = [1, 2, 3, 4]
numbers2 = list(numbers)

print(f'before: {numbers}')
numbers.clear()
print(f'after: {numbers}')

print(f'before: {numbers2}')
del numbers2[:]
print(f'after: {numbers2}')

# solution also has while loop w/ pop() & reassign numbers to empty list w/ caveat
# that og list isn't technically cleared but that's ok if no other refs to it exist