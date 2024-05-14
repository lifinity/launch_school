dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# prints [1, 42, 3] b/c dict2 shallow copy which means 
# 'a' key in both dicts pointing to the same list object in memory