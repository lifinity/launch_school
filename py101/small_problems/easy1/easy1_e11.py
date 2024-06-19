# utf-16 string value
# write function that determines & returns utf-16 str val of a str passed in as arg
# utf-16 str val is the sum of utf-16 val of evry char in the str; use ord() to determine

def utf16_value(str_):
    sum_ = 0
    for chr in str_:
        sum_ += ord(chr)
    return sum_

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)