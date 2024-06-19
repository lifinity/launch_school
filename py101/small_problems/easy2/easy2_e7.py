# exclusive or
# write a xor function that returns True if exactly one arg is truthy, False otherwise

def xor(a, b):
    # one solution returned bool(a) != bool(b); clever
    return bool((a and not b) or (b and not a))

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

# further exploration: situation in which boolean xor useful? also does xor short-circuit,
# why or why not? does short-circuit eval even make any sense?
# answer: any selection option where only one answer allowed, e.g. poll, meal entree/side choice
# also no short-circuit; doesn't make sense because need to eval both to make sure EXACTLY one true