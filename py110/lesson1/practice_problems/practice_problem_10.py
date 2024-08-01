# what does following code print & why
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# prints ('b', 'bear') b/c .popitem() removes & returns
# last-inserted element as tuple (only applicable to python 3.7+)