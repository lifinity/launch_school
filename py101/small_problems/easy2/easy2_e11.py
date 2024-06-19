# get middle character
# write a function that takes non-empty str arg & returns middle character(s)
# if odd length, return exactly 1 char; if even, exactly 2 char

def center_of(str_):
    mid = len(str_) // 2
    return str_[mid-1:mid+1] if len(str_) % 2 == 0 else str_[mid]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True