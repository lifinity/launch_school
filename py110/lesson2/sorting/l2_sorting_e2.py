# sort the following list of numbers first in ascending numeric
# order, then in descending; mutate list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print(lst == [-16, -6, 7, 8, 9, 10, 11, 50])          # Ascending sort
lst.sort(reverse=True)
print(lst == [50, 11, 10, 9, 8, 7, -6, -16])          # Descending sort