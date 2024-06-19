# is empty or blank?
def is_empty_or_blank(str_):
    # return not str_.strip(' ')
    return not str_ or str_.isspace()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True