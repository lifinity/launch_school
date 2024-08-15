# given following data struct, write some code to return list that contains
# colors of fruits & sizes of vegetables; sizes should be uppercase & colors
# should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def derive_produce(dict_):
    return [color.capitalize() for color in dict_['colors']] \
           if dict_['type'] == 'fruit' else dict_['size'].upper()

print([derive_produce(produce_info) for produce_info in dict1.values()])