# the end is near but not here
# write a function that returns the 2nd to last word in the string argument
# words are any seq of non-blank characters; assume input always has 2+ words

def penultimate(str_):
    return str_.split()[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

# further exploration: our assumption allowed us to ignore 0-1 word edge cases;
# what if function that retrieves middle word? what edge cases & how to handle?
# cases: empty str (return empty str), one word (return sole word), 
# even str (return both middle words), odd str (return middle)

def middle_word(str_):
    words = str_.split()
    match len(words):
        case 0: return ""
        case 1: return words[0]
    
    midpoint = len(words) // 2
    if len(words) % 2 == 0:
        return [words[midpoint-1], words[midpoint]]

    return words[midpoint]

print(middle_word(" "))
print(middle_word("We "))
print(middle_word("We are"))
print(middle_word("We are pirates"))
print(middle_word("we are pirates of"))