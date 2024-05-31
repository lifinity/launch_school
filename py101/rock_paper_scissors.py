import random
from os import system

# constants
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

CHOICES = [ROCK, PAPER, SCISSORS]
NUM_CHOICES = [str(num) for num in range(1, len(CHOICES)+1)]
CHAR_CHOICES = [choice[0] for choice in CHOICES]

VALID_CHOICES = dict(zip(CHOICES, CHOICES)) \
              | dict(zip(NUM_CHOICES, CHOICES)) \
              | dict(zip(CHAR_CHOICES, CHOICES)) \

FORMATTED_CHOICE_STRS = [f'{num}) {choice.capitalize()}' for num, choice \
                     in zip(NUM_CHOICES, CHOICES)]

P1_WIN_CONDITIONS = [
                    (ROCK, SCISSORS),
                    (PAPER, ROCK),
                    (SCISSORS, PAPER),
                    ]

Y = 'y'
N = 'n'
VALID_CONTINUE_OPTIONS = [Y, N]

# function definitions
def display_prompt(msg):
    print(f'==> {msg}')

def display_intro():
    system('clear')
    display_prompt("Rock Paper Scissors Game")
    print("------------------------------",
          "------------------------------", sep='')

def display_winner(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        winner_str = "It's a tie."
    elif (p1_choice.casefold(), p2_choice.casefold()) in P1_WIN_CONDITIONS:
        winner_str = "You win!"
    else:
        winner_str = "Computer wins..."
    display_prompt(f'You chose {p1_choice}, ' \
                 + f'computer chose {p2_choice}. {winner_str}')

def get_user_choice():
    display_prompt(f'Choose one: {", ".join(FORMATTED_CHOICE_STRS)}')
    while True:
        user_choice = input().casefold()
        if user_choice in VALID_CHOICES.keys():
            return VALID_CHOICES[user_choice].capitalize()
        display_prompt('Invalid input. You can only choose ' \
                    + f'from: {", ".join(FORMATTED_CHOICE_STRS)}')

def get_computer_choice():
    computer_choice = random.choice(CHOICES)
    return computer_choice.capitalize()

def get_continue():
    display_prompt(f"Would you like to play again, {Y}/{N}?")
    while True:
        keep_going = input().casefold()
        if keep_going[0] in VALID_CONTINUE_OPTIONS:
            return bool(keep_going[0] == Y)
        display_prompt(f"Please answer '{Y}' or '{N}'.")

# main program body
def rock_paper_scissors():
    while True:
        display_intro()
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_winner(user_choice, computer_choice)

        if not get_continue():
            break

if __name__ == "__main__":
    rock_paper_scissors()

# PERSONAL PROJECT NOTES
# -----------------------------------------
# things to consider:
# Q: what happens if you move a display_prompt()'s def to be after another
# function that calls it?
# A: still works as long as an invocation of that other function doesn't
# happen before display_prompt()'s definition

# Q: how would you use display_winner() differently if it returned a string
# as opposed to outputting the string directly
# A: pass it into display_prompt() which'll use the string as part of its
# output to the terminal

# Q: we used a while loop w/ an always true condition & a break statement; can
# you rewrite so we don't need to use a break statement?
# A: define a variable `keep_going = True` outside the loop & set the while
# condition to be `while keep_going`, then adjust the val of keep_going based
# on user input inside the loop. once the loop condition falsy, i.e. when the
# val of keep_going set to False (assuming bool conversion), loop stops running
