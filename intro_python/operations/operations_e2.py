num = 4936
ones = num % 10

num = num // 10
tens = num % 10

num = num // 10
hundreds = num % 10

thousands = num // 10

print(f'One place is {ones}')
print(f'Tens place is {tens}')
print(f'Hundreds place is {hundreds}')
print(f'Thousands place is {thousands}')