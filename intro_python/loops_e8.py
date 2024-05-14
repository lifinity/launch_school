my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = { e: len(e) for e in my_set if len(e) % 2}
print(my_dict)