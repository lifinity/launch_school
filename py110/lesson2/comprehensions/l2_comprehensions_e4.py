# given following data struct, write some code that defines a dict
# where the key is first item in sublist & value is the second

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

print({e[0]: e[1] for e in lst})