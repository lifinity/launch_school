# ddaaiillyy ddoouubbllee
# write a function that takes a str arg & returns new str that contains val
# of original str w/ all consecutive duplicate chars collapsed into single char

import re

def display_divider():
    print('-' * 30)

def crunch(str_):
    result = ''

    for chr in str_:
        if not result or result[-1] != chr:
            result += chr
        
    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

display_divider()

# further exploration; do this w/ regex via re module, or any
# alternative solutions, e.g. using built-in str or list methods

def crunch2(str_):
    result = ''
    while len(str_) > 0:
        current_chr = str_[0]
        result += current_chr
        str_ = str_.lstrip(current_chr)
    return result

# These examples should all print True
print(crunch2('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch2('4444abcabccba') == '4abcabcba')
print(crunch2('ggggggggggggggg') == 'g')
print(crunch2('abc') == 'abc')
print(crunch2('a') == 'a')
print(crunch2('') == '')

display_divider()

# should study regex more... 
def crunch_regex(str_):
    return re.sub(r'(.)\1+', r'\1', str_)

# These examples should all print True
print(crunch_regex('ddaaa$$llyyy   ddoouubbllee') == 'da$ly double')
print(crunch_regex('4444abcabccba') == '4abcabcba')
print(crunch_regex('ggggggggggggggg') == 'g')
print(crunch_regex('abc') == 'abc')
print(crunch_regex('a') == 'a')
print(crunch_regex('') == '')