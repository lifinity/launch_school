# given the following data structure, return new list identical in
# structure but w/ each num += 1; don't mutate & use comprehension

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

print([{key: val + 1 for key, val in nested.items()} for nested in lst])

# can also split dict comprehension part into separate function that you
# run on list comprehension vals, e.g. [increment_values(e) for e in lst]