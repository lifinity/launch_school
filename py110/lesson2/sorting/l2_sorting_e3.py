# sort the following list of numbers first in ascending numeric
# order, then in descending; mutate list & sort as str vals but
# list passed as arg & returned list should contain nums, not str

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
print(lst == [-16, -6, 10, 11, 50, 7, 8, 9])          # Ascending sort
lst.sort(key=str, reverse=True)
print(lst == [9, 8, 7, 50, 11, 10, -6, -16])          # Descending sort