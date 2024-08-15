# for each obj shown below, demonstrate how you'd access letter 'g'
lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

# answer 1
print(lst1[2][1][3])

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

# answer 2
print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

# answer 3
print(lst3[2]['third'][0][0])

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# answer 4
print(dict1['b'][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

# answer 5
print(list(dict2['3rd'].keys())[0])