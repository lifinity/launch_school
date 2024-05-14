# is empty?
def is_empty(str):
    # return str == ""
    # return len(str) < 1
    return not str

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True