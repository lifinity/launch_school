# last element
def last(list_):
    return list_[-1] if list_ else None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))                         # None