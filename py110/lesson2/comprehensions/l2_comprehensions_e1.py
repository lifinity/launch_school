# given following dict, compute and display total age of family's male members
# try solving first w/ ordinary loop first then with comprehension

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# for loop
sum_male_ages = 0
for mem_info in munsters.values():
    if mem_info['gender'] == 'male':
        sum_male_ages += mem_info['age']
print(sum_male_ages)

# comprehension
print(sum([mem_info['age'] for mem_info in munsters.values() \
           if mem_info['gender'] == 'male']))
