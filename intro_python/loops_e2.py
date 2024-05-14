# not named age.py & also effectively rewriting the same program b/c used a loop then too
user_age = int(input('How old are you? '))

print(f'You are {user_age} years old.')
for yr in range(10, 50, 10):
    print(f'In {yr} years, you will be {user_age + yr} years old.')