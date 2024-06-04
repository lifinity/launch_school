def factorial(n):
    result = 1
    for num in range(1, n+1):    # can also do range(n,0,-1)
        result *= num
    return result

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))