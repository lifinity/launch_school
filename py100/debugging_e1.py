# reading error messages
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)    # TypeError; too many args, only 1 param
find_first_nonzero_among(1)                   # TypeError; arg provided not an iterable