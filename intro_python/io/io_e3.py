# age.py except not named that; kind of already wrote this for the og exercise
age = int(input('How old are you? '))
print(f'You are {age} years old.')
for yr in range(10, 50, 10):
    print(f'In {yr} years, you will be {age + yr} years old.')