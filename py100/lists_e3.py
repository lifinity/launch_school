# add + delete
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

print(f'original: {energy}')
energy.remove('fossil')
print(f'removed fossil: {energy}')
energy.append('geothermal')
print(f'added geothermal: {energy}')