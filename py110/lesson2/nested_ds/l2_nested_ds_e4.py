# one of most frequently used real-world str ops is substitution
# i.e. take hard-coded str & modify w/ various params from our program
# given following ob, print name, age & gender of each family member

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# output should follow: (name) is a (age)-year-old (male or female).

for member, details in munsters.items():
    print(f"{member} is a {details['age']}-year-old {details['gender']}.")