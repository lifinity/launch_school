# letter swap
# given string of words separated by spaces, write function that swaps
# first & last letters of every word. assume every word has at least 1
# letter & string will always contain at least one word & each string
# has nothing but words & spaces + no leading, trailing or repeated spaces

# input: str
# output: str w/ 1st & last letters of every word swapped

# explicit rules
# - every word has at least 1 letter
# - input string will always have at least one word (no empty strings)
# - input string has nothing but words & spaces
# - there are no leading, trailing or repeated spaces

# implicit rules
# - words are separated by spaces
# - preserve the original case of characters
# - preserve spacing of words in output 

# questions (theoretical)
# - max length of overall string or words?

# data structures
# list as intermediary for transforming words in string
# alt; can generate and return a new str (worse opt b/c space preservation req)

# algorithm
# 1. get all words in string
# 2. for every word, switch first & last characters
# 3. combine all the transformed words into a single string again and return

def swap(str_):
    words = str_.split()
    swapped = ' '.join([word if len(word) < 2 else \
                       (word[-1] + word[1:-1] + word[0]) \
                       for word in words])
    return swapped

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True