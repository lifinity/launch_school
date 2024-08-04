# palindromic strings (part 2)
# write a function that returns bool re: whether arg str is palindrome
# BUT this time, case-insensitive & ignore all non-alphanum characters
# can reuse/call is_palindrome from prev exercise (easy1_e2)

# input: str
# output: bool (True if input str palindrome, False otherwise)

# explicit rules
# - palindrome is str that reads the same forward & back
# - case-insensitive, e.g. 'Madam' & 'madam' both palindromes
# - ignore all non-alphanums, e.g. '356635' palindrome b/c 
# stripping out all nums -> empty str -> same forward & back

# implicit rules
# - empty strings should be treated as palindromes
# - whitespace counts as non-alphanum

# questions (theoretical)
# !! does alphanum encapsulate international alphabets or just ascii?

# data structures
# list b/c wanna use list comprehension to strip out non-alphanum
# !! could also empty str & loop to rebuild w/ only alphanum; or regex

# algorithm
# 1. casefold input string & remove all non-alphanumeric characters
# 2. compare sanitized str w/ its reverse to determine if palindrome

def is_palindrome(str_):
    return str_ == str_[::-1]

def is_real_palindrome(str_):
    sanitized_strlist = [char.casefold() for char in str_ \
                         if char.isalnum() and char.isascii()]
    return is_palindrome(''.join(sanitized_strlist))

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
