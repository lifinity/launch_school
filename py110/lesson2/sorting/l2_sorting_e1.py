# sort the following list of numbers first in ascending numeric
# order, then in descending. do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

ascending_lst = sorted(lst)
descending_lst = sorted(lst, reverse=True)

print(ascending_lst == [-16, -6, 7, 8, 9, 10, 11, 50])          # Ascending sort
print(descending_lst == [50, 11, 10, 9, 8, 7, -6, -16])         # Descending sort
print(lst == [10, 9, -6, 11, 7, -16, 50, 8])                    # Original list unchanged