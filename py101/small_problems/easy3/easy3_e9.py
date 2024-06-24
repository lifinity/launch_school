# clean up the words
# write function that, given str of mixed words & non-alpha chars, returns it w/ all
# non-alpha char replaced by spaces. if 1+ non-alpha char occur in a row, condense
# down to single space, i.e. never any spaces in a row

def clean_up(str_):
    clean = ""

    for chr in str_:
        # note that isalpha() doesn't discrim against foreign lang alphabet
        # so if you want to exclude them, have to specify isascii() too
        if chr.isalpha():
            clean += chr
        elif not clean or clean[-1] != ' ':
            clean += ' '

    return clean

print(clean_up("---what's my +*& line?") == " what s my line ") # True
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")   # True (False if isascii() included)