# given following data structure, return a new list identical in
# structure to og, but containing only numbers that're multiples of 3

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# for loop; nested
lst2 = []
for sublist in lst:
    new_sublist = []
    for num in sublist:
        if num % 3 == 0:
            new_sublist.append(num)
    lst2.append(new_sublist)
print(lst2)

# comprehension
print([[num for num in sublist if num % 3 == 0] for sublist in lst])

# arguably better practice to extract out nested comprehension into
# separate function that's called on element of outer comprehension
# e.g. [nums_divis_by_3(sublist) for sublist in lst], more readable