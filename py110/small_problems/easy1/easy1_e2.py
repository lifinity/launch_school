# palindromic strings (part 1)
# write function that returns bool re: whether arg str is palindrome
# palindrome reads the same forwards & backwards, case sensitive & all chars matter

# input: str
# output: boolean (True if palindrome, False otherwise)

# explicit rules
# - palindrome is a str that reads the same forward & backwards
# - case sensitive, e.g. 'Madam' not a palindrome but 'madam' is
# - all characters matter; can have numbers & special characters

# implicit rules
# - strings can have spaces, numbers, punctuation & they count

# questions (theoretical)
# - empty string possible as input? counts as palindrome?

# data structures
# !! don't need b/c can directly create reversed str w/ slicing

# algorithm
# 1. compare original string with its reversed version & return result

def is_palindrome(str_):
    return str_ == str_[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)