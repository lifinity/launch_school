# how old is teddy?
# build program that randomly generates & prints teddy's age
# to get age, generate random number between 20 & 100, inclusive

import random

def determine_teddy_age():
    print(f"Teddy is {random.randint(20, 100)} years old!")

determine_teddy_age()

# further exploration: modify program to ask for name, then print age for person
# default to "Teddy" as name if none entered -> can do this in 2 ways, default
# param if 'ask for name' just means taking in additional name argument, or get as
# input() followed by conditional reassign, e.g. name = name if bool(name) else "Teddy"