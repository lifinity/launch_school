# given following str, create letter-frequency dict (case-sensitive)
statement = "The Flintstones Rock"

from pprint import pp

char_frequency = {}
for char in statement.replace(' ', ''):
    char_frequency.setdefault(char, 0)
    char_frequency[char] += 1
pp(char_frequency)

# note; remember to clarify what counts as a letter, e.g. do spaces?