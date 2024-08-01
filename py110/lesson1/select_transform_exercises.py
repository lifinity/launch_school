def print_separator():
    print('-' * 30)

def mutating_double_numbers(numbers):
    for idx in range(len(numbers)):
        numbers[idx] *= 2
    return numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(mutating_double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                          # [2, 8, 6, 14, 4, 12]

print_separator() # ---

def double_odd_index_numbers(numbers):
    doubled_nums = []

    for idx, num in enumerate(numbers):
        if idx % 2 == 1:
            doubled_nums.append(num * 2)
        else:
            doubled_nums.append(num)

    return doubled_nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_index_numbers(my_numbers))  # [1, 8, 3, 14, 2, 12]
print(my_numbers)                            # [1, 4, 3, 7, 2, 6]

print_separator() # ---

def multiply(numbers, multiplier):
    return [num * multiplier for num in numbers]

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
print(my_numbers)               # [1, 4, 3, 7, 2, 6]