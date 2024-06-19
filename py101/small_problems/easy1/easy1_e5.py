# tip calculator
# program should prompt for bill amt & tip rate; must compute tip, then print
# both tip & total amt of bill. can ignore input validation & assume valid #s

def tip_calculator():
    bill_amt = float(input("What is the bill? "))
    tip_percent = float(input("What is the tip percentage? ").strip('%'))

    tip_amt = bill_amt * (tip_percent/100)
    total = bill_amt + tip_amt
    
    print(f'The tip is ${tip_amt:.2f}.')
    print(f'The total is ${total:.2f}.')

tip_calculator()