# q9; given dict of family members & ages, add additional entries as provided
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

print(f'before: {ages}')
ages.update(additional_ages)
print(f'after: {ages}')