# looping over list elements
lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

# nothing printed; loop wouldn't run if lst was empty b/c 0 < 0 falsy