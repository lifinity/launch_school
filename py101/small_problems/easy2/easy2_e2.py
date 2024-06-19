# greeting a user
# write a program that asks for user's name, then greets; if user appends '!'
# to their name, computer will yell greeting (print in all uppercase)

def greet_user():
    user_name = input("What is your name? ")
    if user_name.endswith('!'):
        print(f"Hello {user_name}! Why are we yelling?".upper())
    else: 
       print(f"Hello {user_name}.")

greet_user()