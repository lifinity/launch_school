# is empty?
def is_empty(str_):
    # return str_ == ""
    # return len(str_) < 1
    return not str_

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True