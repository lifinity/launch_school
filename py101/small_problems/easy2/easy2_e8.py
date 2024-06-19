# odd lists
# write function that returns list that contains every other element of list passed
# in as arg, starting from index 0; vals should be 1st, 3rd, 5th, etc elements
# bonus q: try to solve using list slicing

def oddities(list_):
    # return [num for index, num in enumerate(list_) if not index % 2]
    return list_[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print('-' * 30)
# further exploration: write function that returns 2nd, 4th, 6th, etc elements of list
# try to solve this differently from given solutions

def evenlies(list_):
    return [num for index, num in enumerate(list_) if index % 2]

print(evenlies([2, 3, 4, 5, 6, 8]) == [3, 5, 8])  # True
print(evenlies([1, 2, 3, 4]) == [2, 4])        # True
print(evenlies(["abc", "def"]) == ['def'])     # True
print(evenlies([123]) == [])                # True
print(evenlies([]) == [])                      # True