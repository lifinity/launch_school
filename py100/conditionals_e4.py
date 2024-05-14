# check the weather, part 1
import random
weather = random.choice(['sunny', 'rainy', 'armageddon'])

# print(weather)
if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")
