# travel
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(item, list_):
    for e in list_:
        if e == item:
            return True
    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False