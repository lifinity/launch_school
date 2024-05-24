import json

# Open JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt("Select a language. Default is English (en) if improper input.\n \
Options are: en, es, fr, de, cn, jp")
lang_code = input().casefold()

LANGUAGE = lang_code if lang_code in \
  ['en', 'es', 'fr', 'de', 'cn', 'jp'] else 'en'
MESSAGES = data.get(LANGUAGE)

prompt(MESSAGES['welcome'])

while True:
    # Ask the user for the first number.
    prompt(MESSAGES['get_num1'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_num'])
        number1 = input()

    # Ask the user for the second number.
    prompt(MESSAGES['get_num2'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_num'])
        number2 = input()

    # Cast to float for upcoming operations
    number1 = float(number1)
    number2 = float(number2)

    # Ask the user for an operation to perform.
    prompt(MESSAGES['get_operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES['invalid_operation'])
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1': # '1' represents addition
            output = number1 + number2
        case '2': # '2' represents subtraction
            output = number1 - number2
        case '3': # '3' represents multiplication
            output = number1 * number2
        case '4': # '4' represents division
            output = number1 / number2

    # Print the result to the terminal.
    print(MESSAGES['result'] + str(output))

    # Ask user if they want to keep going
    prompt(MESSAGES['get_continue'] + 'Y/N?')
    keep_going = input().casefold()

    while keep_going not in ["y", "yes", "n", "no"]:
        prompt(MESSAGES['invalid_continue'])
        keep_going = input().casefold()

    if keep_going in ["n", "no"]:
        break