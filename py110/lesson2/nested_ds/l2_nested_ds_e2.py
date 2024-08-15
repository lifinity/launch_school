# for each collection obj, demonstrate how you'd change val 3 to 4
lst1 = [1, [2, 3], 4]

# answer 1
lst1[1][1] = lst1[2]
print(lst1)

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

# answer 2
lst2[2] = lst2[1]['d']
print(lst2)

dict1 = {'first': [1, 2, [3]]}

# answer 3
dict1['first'][2][0] = 4
print(dict1)

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

# answer 4
dict2['a']['a'][2] = dict2['a']['b']
print(dict2)

# if there was an existing 4 somewhere, reassigned to it for
# fun and sport; functionally same outcome since ints primitives