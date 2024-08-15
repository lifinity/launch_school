# the following dict has list vals containing strings; write some code
# to create a list of every vowel (a, e, i, o, u) that appears in contained
# strings, then print. start by trying to write w/ nested loops, then
# refactor to use single list comprehension (extra challenge)

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# nested for loop
list_of_vowels = []
for sublist in dict1.values():
    for word in sublist:
        for char in word:
            if char in 'aeiou':
                list_of_vowels.append(char)
print(list_of_vowels)

# nested comprehension
VOWELS = 'aeiou'
print([char for sublist in dict1.values()
            for string in sublist
            for char in string if char.casefold() in VOWELS])

# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']