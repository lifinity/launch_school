# given the following data struct, return a NEW list w/ same
# structure but vals in each sublist ordered in ascending order
# try using for loop first but use comprehension if you can

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# for loop
lst2 = []
for sublist in lst:
    sublist.sort() # mutates
    lst2.append(sublist)
print(lst2)

# comprehension
print([sorted(sublist) for sublist in lst])