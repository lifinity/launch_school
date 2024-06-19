# when will i retire
# build program that displays when user will retire & how many yrs left to work
from datetime import datetime as dt

def valid_number(num):
    try:
        if int(num) <= 0:
            raise ValueError
    except ValueError:
        return False
    return True

def get_num(prompt):
    num_input = input(prompt)

    while not valid_number(num_input):
        print("That's not a valid number. Positive whole numbers only please.")
        num_input = input(prompt)

    return int(num_input)

def retirement_calc():
    age = get_num("What is your age? ")
    retirement_age = get_num("What age would you like to retire? ")

    current_year = dt.now().year
    years_left = retirement_age - age

    # note: don't really handle case where retirement age <= age atm
    print(f"It's {current_year}. You will retire in {current_year + years_left}.",
          f"You only have {years_left} years of work to go!", sep="\n")
    
retirement_calc()

