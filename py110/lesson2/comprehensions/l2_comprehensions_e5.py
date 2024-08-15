# given following data struct, sort the list so the sub-lists
# are ordered based on sum of odd numbers they contain; don't mutate

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sort_by_odds_sum(list_):
    return sum([num for num in list_ if num % 2])

print(sorted(lst, key=sort_by_odds_sum))