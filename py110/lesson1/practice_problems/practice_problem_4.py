# given the following code, what's the output w/o running
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# prints a dict where namestrings are keys and vals are
# the (last) index that name occurs at in the names list