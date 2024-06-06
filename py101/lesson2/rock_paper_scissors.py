import random
from math import ceil
from os import system

# constants
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
LIZARD = 'lizard'
SPOCK = 'spock'

CHOICES = [ROCK, PAPER, SCISSORS, LIZARD, SPOCK]
NUM_CHOICES = [str(num) for num in range(1, len(CHOICES)+1)]
CHAR_CHOICES = [(choice[0] if choice[0] != 's'
                else choice[:2]) for choice in CHOICES]

VALID_CHOICES = dict(zip(CHOICES, CHOICES)) \
              | dict(zip(NUM_CHOICES, CHOICES)) \
              | dict(zip(CHAR_CHOICES, CHOICES)) \

WIN_CONDITIONS = {
                  ROCK: [SCISSORS, LIZARD],
                  PAPER: [ROCK, SPOCK],
                  SCISSORS: [PAPER, LIZARD],
                  LIZARD: [PAPER, SPOCK],
                  SPOCK: [ROCK, SCISSORS],
                 }

VALID_CONTINUE_OPTIONS = ['y', 'yes', 'no', 'n']

WON = 'w'
LOST = 'l'
TIE = 't'

PLAYER1 = 'p1'
PLAYER2 = 'p2'
DELIMITER = '_'

NUM_MATCH_ROUNDS = 5

# display/print functions
def display_prefix(msg, prefix='==>'):
    print(f'{prefix} {msg}')

def print_separator():
    print("-" * 60, sep='')

def display_game_intro():
    system('clear')
    display_prefix("Rock Paper Scissors Lizard Spock " \
                + f"(Best of {NUM_MATCH_ROUNDS})")
    print_separator()
    print_rules()
    print_separator()

def print_rules():
    display_prefix("Game Rules", '>>')
    for idx, (key, val) in enumerate(WIN_CONDITIONS.items()):
        print(f'{idx+1}) {key.capitalize()} beats ' \
            + f'{" & ".join([choice.capitalize() for choice in val])}')

def display_round_intro(round_num, match_history):
    display_prefix(f"Round {round_num}; " \
                 + f"{generate_score_str(match_history)}", '-->')

def print_round_results(p1_choice, p2_choice, outcome):
    print(f'You chose {p1_choice.capitalize()},',
          f'Computer chose {p2_choice.capitalize()}.',
          generate_outcome_str(outcome))
    print_separator()

def display_match_results(match_history):
    outcome = calc_match_winner(match_history)
    display_prefix(f'MATCH RESULTS: {generate_score_str(match_history)}. ' \
                 + f'{generate_outcome_str(outcome)}', '!!!')

# string mapping helper functions
def generate_outcome_str(outcome):
    if outcome == WON:
        return "You win!"
    if outcome == LOST:
        return "Computer wins..."
    return "It's a tie."

def generate_score_str(match_history):
    p1_wins = retrieve_num_wins(PLAYER1, match_history)
    p2_wins = retrieve_num_wins(PLAYER2, match_history)
    return f'You: {p1_wins} versus Computer: {p2_wins}'

# user input functions
def get_user_choice():
    choice_strs = [f'{num}) {choice.capitalize()}' \
                  for num, choice in zip(NUM_CHOICES, CHOICES)]
    display_prefix(f'Choose one: {", ".join(choice_strs)}')
    while True:
        user_choice = input().casefold()
        if user_choice in VALID_CHOICES.keys():
            return VALID_CHOICES[user_choice]
        display_prefix('Invalid input. You can only choose ' \
                    + f'from: {", ".join(choice_strs)}')

def get_computer_choice():
    computer_choice = random.choice(CHOICES)
    return computer_choice

def get_continue():
    display_prefix("Would you like to play another match, y/n?")
    while True:
        keep_going = input().casefold()
        if keep_going in VALID_CONTINUE_OPTIONS:
            return bool(keep_going in VALID_CONTINUE_OPTIONS[:2])
        display_prefix("Please answer 'yes'/'y' or 'no'/'n'.")

# match history functions
def retrieve_num_wins(player_key, match_history):
    if len(match_history[player_key]) < 1:
        return 0
    return match_history[player_key][-1].split(DELIMITER)[-1]

def update_match_history(player_key, player_choice, outcome, match_history):
    num_wins = int(retrieve_num_wins(player_key, match_history))
    if outcome == WON:
        num_wins += 1
    round_record = f'{player_choice}{DELIMITER}{outcome}{DELIMITER}{num_wins}'
    match_history[player_key].append(round_record)

def reset_match_history(match_history):
    for player_record in match_history.values():
        player_record.clear()

# calculate game state functions
def calc_round_winner(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return (TIE, TIE)
    if p2_choice in WIN_CONDITIONS[p1_choice]:
        return (WON, LOST)
    return (LOST, WON)

def calc_match_winner(match_history):
    p1_score = retrieve_num_wins(PLAYER1, match_history)
    p2_score = retrieve_num_wins(PLAYER2, match_history)
    if p1_score == p2_score:
        return TIE
    if p1_score > p2_score:
        return WON
    return LOST

def calc_match_over(match_history):
    p1_score = int(retrieve_num_wins(PLAYER1, match_history))
    p2_score = int(retrieve_num_wins(PLAYER2, match_history))
    halfway_point = ceil(NUM_MATCH_ROUNDS / 2)
    end_early_point = halfway_point if halfway_point % 2 else halfway_point + 1
    return bool(p1_score >= end_early_point
             or p2_score >= end_early_point)

# subroutine for playing one round of the game
def play_round(round_num, match_history):
    display_round_intro(round_num, match_history)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    p1_outcome, p2_outcome = calc_round_winner(user_choice, computer_choice)
    update_match_history(PLAYER1, user_choice, p1_outcome, match_history)
    update_match_history(PLAYER2, computer_choice, p2_outcome, match_history)
    print_round_results(user_choice, computer_choice, p1_outcome)

# main program body
def rock_paper_scissors():
    while True:
        display_game_intro()

        round_num = 1
        match_history = { PLAYER1: [], PLAYER2: [] }
        # e.g. 'p1': ['rock_w_1', 'scissors_l_1', ...]
        while round_num <= NUM_MATCH_ROUNDS and \
              not calc_match_over(match_history):
            play_round(round_num, match_history)
            round_num += 1

        display_match_results(match_history)
        reset_match_history(match_history)

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

# lizard spock:
# rock beats scissor & lizard
# paper beats rock & spock
# scissor beats paper & lizard
# lizard beats paper & spock
# spock beats rock & scissor

# best of 5:
# match history dictionary recording moves, round outcome, player win #
# loop & keep playing rounds until someone has 3 wins; update dict as you go
# print match results, clear dict & ask user if they want to play another match