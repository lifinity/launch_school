import json
from os import system
from math import isnan

# constant definitions
MONTHS_IN_YEAR = 12
MAX_LOAN = 1_000_000_000
MAX_APR = 100
MIN_DURATION = 1
MAX_DURATION = 100

# load in external prompt/error msgs from JSON
with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# function definitions
def display_prompt(msg_key, extra_msg=''):
    msg = MESSAGES[msg_key] if msg_key else ''
    print(f'==> {msg}{extra_msg}')

def valid_number(num_str, num_ceiling, num_floor=0, num_type='float'):
    try:
        num = int(num_str) if num_type == 'int' else float(num_str)
        if isnan(num) or num > num_ceiling or num < num_floor:
            raise ValueError
    except ValueError:
        return False

    return True

def get_loan_amount():
    display_prompt('get_loan_amount')
    while True:
        loan_amount_str = input().strip('$').replace(',', '')
        if valid_number(loan_amount_str, MAX_LOAN):
            return float(loan_amount_str)
        display_prompt('invalid_number')

def get_annual_percent():
    display_prompt('get_annual_percent')
    while True:
        annual_percentage_str = input().strip('%')
        if valid_number(annual_percentage_str, MAX_APR):
            return float(annual_percentage_str)
        display_prompt('invalid_number')

def get_loan_duration():
    display_prompt('get_loan_duration')
    while True:
        loan_duration_str = input()
        if valid_number(loan_duration_str, MAX_DURATION,
                        MIN_DURATION, 'int'):
            return int(loan_duration_str)
        display_prompt('invalid_duration')

def get_continue():
    display_prompt('get_continue', 'y/n?')
    while True:
        keep_going = input().casefold()
        if keep_going in ["y", "yes", "n", "no"]:
            return bool(keep_going[0] == 'y')
        display_prompt('invalid_continue' + "'yes'/'y' or 'no'/'n'")

# main program definition
def loan_calculator():
    while True:
        # display program intro; clear first for consistent display
        system('clear')
        display_prompt('welcome')
        print("------------------------------",
              "------------------------------", sep='')

        # get loan amount from user
        loan_amount = get_loan_amount()

        if loan_amount > 0:
            # get annual percentage rate from user
            annual_percent = get_annual_percent()
            monthly_percent = (annual_percent / 100) / MONTHS_IN_YEAR

            # get loan duration rate from user
            loan_duration_months = get_loan_duration()

            if monthly_percent > 0:
                # calculate monthly payment w/ provided inputs
                loan_payment = loan_amount * (monthly_percent / \
                (1 - (1 + monthly_percent)**(-loan_duration_months)))
            else:
                # handle 0-interest edge case
                loan_payment = loan_amount/loan_duration_months
        else:
            # handle 0-loan amount edge case;
            loan_payment = 0

        # display input recap & calculation results
        display_prompt(None, f'${loan_amount:.2f} @ {annual_percent:.2f}% ' \
                       + f'APR for {loan_duration_months} months.')
        display_prompt('loan_payment', f'${loan_payment:.2f}')

        # ask user if they want to run another calculation
        if not get_continue():
            break

# run main program
if __name__ == "__main__":
    loan_calculator()

# PERSONAL PROJECT NOTES
# -----------------------------------------
# user input:
# loan amount (float; int ok too)
# annual percentage rate (apr) (pre-processed float, i.e. 5 & not .05)
# loan duration (int, months only)

# calculate:
# monthly interest rate (apr/100)/12
# loan duration in months (no calc; input already in months)

# loan_payment = loan_amount * (monthly_interest_rate /
# (1 - (1 + monthly_interest_rate)**loan_duration_months))
# print payment as dollar & cents (float, rounded to 2 decimals)

# edge cases:
# negative inputs (not allowed)
# 0 inputs; loan amount 0 (ok), apr 0 (ok), loan duration 0 (no)
# loans that aren't int # yrs, aka decimals? (no, whole months only)
# nan & inf; should upper bound certain values e.g. apr @ 100