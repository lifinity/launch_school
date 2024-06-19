# short long short
# write a function that takes 2 str as args, determines their length and
# returns result of concatenating shorter str + longer + shorter again
# can assume strs are of different lengths

def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    return str2 + str1 + str2

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")