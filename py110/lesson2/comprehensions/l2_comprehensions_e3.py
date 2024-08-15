# given following data struct, return NEW list w/ same structure
# but w/ vals in each sublist ordered in ascending order as strings
# i.e. nums should be treated as str; for loop 1st, then comprehension

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# for loop
lst2 = []
for sublist in lst:
    sublist.sort(key=str)
    lst2.append(sublist)
print(lst2)

# comprehension
print([sorted(sublist, key=str) for sublist in lst])