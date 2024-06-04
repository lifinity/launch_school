dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# prints 'The Life of Brian' b/c dict2 initialized w/ a shallow copy of dict1
# and since none of the vals are nested mutable collections, no shared ref happening here