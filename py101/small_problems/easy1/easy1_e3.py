# even numbers
# print all even #s from 1 - 99 inclusive w/ each num on separate line
# bonus q: solve by iterating over just even numbers?

def display_evens(start, end):
    adjusted_start = start if start % 2 == 0 else start + 1
    for even_num in range(adjusted_start, end+1, 2):
        print(even_num)

display_evens(1, 99)