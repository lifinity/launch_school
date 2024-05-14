def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# dictionary.keys() provides a dict view list of all the keys
# sorted() returns a new sorted list of the keys: 
# ['Antonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor']
# [1] accesses the list element @ index 1: 'Chris'
# str.upper() method is run on the element, capitalizing it: 'CHRIS'
# & that capitalized string is returned to be printed out