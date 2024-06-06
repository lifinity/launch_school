# q1; 2 distinct ways of reverse list w/o mutating original list
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

numbers2 = [num for num in reversed(numbers)]
print(numbers2)
numbers3 = sorted(numbers, reverse=True)
print(numbers3)
numbers4 = numbers[::-1]
print(numbers4)
print(numbers)

# solution used list(reversed(numbers)), cleaner than list comprehension