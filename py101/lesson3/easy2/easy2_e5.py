# q5; how to verify whether data structs assigned to given variables are of type list?
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list)
print(type(table) is list)

# isinstance(var_name, list) preferred b/c faster & considers inheritance