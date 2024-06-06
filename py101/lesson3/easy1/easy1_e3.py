# q3; given str, 2 diff ways to make new str w/ 'Four score and ' prepended
famous_words = "seven years ago..."
prefix = 'Four score and '

print(prefix + famous_words)
print(f'{prefix}{famous_words}')
print(''.join([prefix, famous_words]))
