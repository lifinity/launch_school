# letter counter (part 1)
# write a function that takes a str consisting of 0+ space-separated words
# and returns a dictionary that shows num of words of diff sizes

# input: str
# output: dict

# explicit rules
# - words are separated by spaces
# - output dict needs to keep track of how many words in the input
# string are of length n, where n is some arbitrary length

# implicit rules
# - empty input strings allowed & should return empty dict

# questions (theoretical)
# - maximum length of string or of word in string?
# - is it possible to have consecutive spaces & expected behavior if yes?
# (assumption: 1 space behaviorally equiv to 1+ spaces re: breaking up words)

# data structures
# dict; expected output format. key = len(word) & val = num words of that length

# algorithm
# 1. get all the words from the string
# 2. for every word, figure out size and tally in the dictionary
# 3. return dictionary of word-size frequency counts

def word_sizes(str_):
    words = str_.split()
    word_size_tally = {}

    for word in words:
        word_size = len(word)
        word_size_tally.setdefault(word_size, 0)
        word_size_tally[word_size] += 1
        
    return word_size_tally

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})