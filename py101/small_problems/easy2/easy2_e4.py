# squaring an argument
# using multiply function from prev exercise, write function that computes
# square of its argument, i.e. result of multiplying number by itself

def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

# further exploration: generalize to 'power to the n' func still using multiply
def num_to_n_power(num, n):
    total = 1
    for _ in range(n):
        total = multiply(total, num)
    return total

print(num_to_n_power(3, 0)) # 3^0 = 1
print(num_to_n_power(3, 1)) # 3^1 = 3
print(num_to_n_power(3, 2)) # 3^2 = 9
print(num_to_n_power(3, 3)) # 3^3 = 27
