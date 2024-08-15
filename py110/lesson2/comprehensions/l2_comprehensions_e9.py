# given following data struct, write some code to return a list that
# contains only the dictionaries where all numbers are even

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def has_odd_num(list_):
    for num in list_:
        if num % 2:
            return True
    return False

def all_sublists_even(dict_):
    for list in dict_.values():
        if has_odd_num(list):
            return False
    return True

print([subdict for subdict in lst if all_sublists_even(subdict)])

# alt solution using built-in all()
def all_even(dict_):
    for sublist in dict_.values():
        if not all([num % 2 == 0 for num in sublist]):
            return False
    return True

print([subdict for subdict in lst if all_even(subdict)])