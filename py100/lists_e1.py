# first element
def first(list_):
    return list_[0] if list_ else None

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))                         # None