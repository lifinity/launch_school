# letter counter (part 2)
# modify word_sizes function from prev exercise (easy1_e5) to exclude
# non-letters when determining word size, e.g. size of 'it's' should be 3, NOT 4

# input: str
# output: dict

# explicit rules
# - words are separated by spaces
# - output dict needs to keep track of how many words in the input
# string are of 'size' n, where n is some arbitrary length
# - non-alpha don't count towards word size

# implicit rules
# - empty input strings allowed & should return empty dict

# questions (theoretical)
# - maximum length of string or of word in string?
# - is it possible to have consecutive spaces & expected behavior if yes?
# (assumption: 1 space behaviorally equiv to 1+ spaces re: breaking up words)
# - definition of a 'letter'; only alphabet char? only ascii? (yes & no?)

# data structures
# dict; expected output format. key = len(word) & val = num words of that length

# algorithm
# 1. get all the words from the string
# 2. for every word, figure out size after removing non-letters
# 3. tally size in dictionary & return dict @ loop end

# note: played with using regex; re.sub('[^a-zA-Z\s]+', '', str_) replaces all chars
# that aren't one or more instances of a-z, A-Z, or \s (whitespace) w/ empty str ''
# ultimately decided not to b/c not inclusive of internationalized 'letters' w/o more work

def strip_nonletters(str_):
    return ''.join([char for char in str_ if char.isalpha()])

print(strip_nonletters("h@llo") == "hllo")
print(strip_nonletters("35ny") == "ny")
print(strip_nonletters("") == "")
print(strip_nonletters("@34$1*∆") == "")
print(strip_nonletters("åugh") == "åugh")

print('-' * 10 )

def word_sizes(str_):
    words = str_.split()
    word_size_tally = {}

    for word in words:
        word_size = len(strip_nonletters(word))
        word_size_tally.setdefault(word_size, 0)
        word_size_tally[word_size] += 1
        
    return word_size_tally

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})