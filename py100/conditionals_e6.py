# check the weather, part 2
import random
weather = random.choice(['sunny', 'rainy', 'snowy', 'blizzard', 'armageddon'])

# print(weather)
match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case 'snowy' | 'blizzard':
        print("Wow... time to shovel.")
    case _:
        print("Let's stay inside.")