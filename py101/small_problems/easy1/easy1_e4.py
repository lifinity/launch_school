# how big is the room?
# build program that asks user to enter length & width of a room 
# in meters, then prints room's area in: square meters & square feet

SQUARE_FEET_PER_SQUARE_METER = 10.7639
VALID_UNIT_INPUTS = ['m', 'meters', 'feet', 'ft']

def valid_number(num):
    try:
        float(num)
    except ValueError:
        return False
    return True

def get_num_input(prompt):
    num_input = input(prompt)

    while not valid_number(num_input):
        print("That's not a valid number.")
        num_input = input(prompt)

    return abs(float(num_input))

def get_unit_input(prompt):
    unit_input = input(prompt)

    while unit_input not in VALID_UNIT_INPUTS:
        print("Invalid unit entered. Enter 'meters' or 'feet'.")
        unit_input = input(prompt)
    
    return unit_input

# futher exploration: mod program to let user specify measurement type (meters/feet)
# computer area accordingly & print it & its conversion in parentheses
def determine_area():
    units = get_unit_input("Calculate area in 'meters' or 'feet'? ")
    length = get_num_input("Enter length of your room (numbers only): ")
    width = get_num_input("Enter width of your room (numbers only): ")

    area_unit1 = length * width

    if units in VALID_UNIT_INPUTS[:2]:
        area_unit2 = area_unit1 * SQUARE_FEET_PER_SQUARE_METER
        alt_unit = VALID_UNIT_INPUTS[-1]
    else:
        area_unit2 = area_unit1 / SQUARE_FEET_PER_SQUARE_METER
        alt_unit = VALID_UNIT_INPUTS[0]

    print(f'The area of your {length:.2f} {units} long, {width:.2f} {units} wide room is',
          f'{area_unit1:.2f} {units} squared ({area_unit2:.2f} {alt_unit} squared)')
    
determine_area()