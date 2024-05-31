import json
from os import system
from math import isnan, ceil

# constant definitions
MONTHS_IN_YEAR = 12
MAX_LOAN = 1_000_000_000
MAX_APR = 100
MIN_DURATION = 0.5
MAX_DURATION = 100
VALID_CONTINUE_OPTIONS = ["y", "yes", "n", "no"]

# load in external prompt/error msgs from JSON
with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# function definitions
def display_intro():
    system('clear') # clear first for consistent display
    display_prompt('welcome')
    print("------------------------------",
          "------------------------------", sep='')

def display_prompt(msg_key, extra_msg=''):
    msg = MESSAGES[msg_key] if msg_key else ''
    print(f'==> {msg}{extra_msg}')

def display_recap(loan_amount, annual_percent,
                  loan_duration_years, loan_duration_months):
    display_prompt(None, f'${loan_amount:.2f} @ {annual_percent:.2f}% ' \
                       + f'APR for {loan_duration_years:.2f} years ' \
                       + f'({loan_duration_months:.0f} months).')

def display_payment(loan_payment):
    display_prompt('loan_payment', f'${loan_payment:.2f}')

def valid_number(num_str, num_ceiling, num_floor=0):
    try:
        num = float(num_str)
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
        display_prompt('invalid_loan_amount')

def get_annual_percent():
    display_prompt('get_annual_percent')
    while True:
        annual_percent_str = input().strip('%')
        if valid_number(annual_percent_str, MAX_APR):
            return float(annual_percent_str)
        display_prompt('invalid_annual_percent')

def get_loan_duration():
    display_prompt('get_loan_duration')
    while True:
        loan_duration_str = input()
        if valid_number(loan_duration_str, MAX_DURATION, MIN_DURATION):
            return float(loan_duration_str)
        display_prompt('invalid_duration')

def get_continue():
    display_prompt('get_continue', 'y/n?')
    while True:
        keep_going = input().casefold()
        if keep_going in VALID_CONTINUE_OPTIONS:
            return bool(keep_going[0] == 'y')
        display_prompt('invalid_continue', "'yes'/'y' or 'no'/'n'")

def calc_monthly_percent(annual_percent):
    return (annual_percent / 100) / MONTHS_IN_YEAR

def calc_duration_months(loan_duration_years):
    return ceil(loan_duration_years * 12)

def calc_payment(loan_amount, monthly_percent, loan_duration_months):
    denominator = (1 - (1 + monthly_percent)**(-loan_duration_months))
    return loan_amount * (monthly_percent / denominator)

# main program definition
def loan_calculator():
    while True:
        display_intro()

        loan_amount = get_loan_amount()
        if loan_amount > 0:
            annual_percent = get_annual_percent()
            monthly_percent = calc_monthly_percent(annual_percent)
            loan_duration_years = get_loan_duration()
            loan_duration_months = calc_duration_months(loan_duration_years)
            if monthly_percent > 0:
                loan_payment = calc_payment(loan_amount, monthly_percent,
                                            loan_duration_months)
            else: # handle 0-interest edge case
                loan_payment = loan_amount/loan_duration_months
        else: # handle 0-loan amount edge case;
            loan_payment = 0

        if loan_payment > 0:
            display_recap(loan_amount, annual_percent,
                          loan_duration_years, loan_duration_months)
        display_payment(loan_payment)

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
# loan duration (float)

# calculate:
# monthly interest rate (apr/100)/12
# loan duration in months (yrs * 12, rounded up)

# loan_payment = loan_amount * (monthly_interest_rate /
# (1 - (1 + monthly_interest_rate)**loan_duration_months))
# print payment as dollar & cents (float, rounded to 2 decimals)

# edge cases:
# negative inputs (not allowed)
# 0 inputs; loan amount 0 (ok), apr 0 (ok), loan duration 0 (no)
# loans that aren't int # yrs, aka decimals? (yeah ok)
# nan & inf; should upper bound certain values e.g. apr @ 100