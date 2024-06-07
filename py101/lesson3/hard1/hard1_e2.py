# q2; what does the last line in the following code output?
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# the last line outputs {'first': [1, 2]} b/c assigning dictionary['first']
# to num_list means it references the object that lives there, therefore the
# method call to append 2 on line 4 mutates the object num_list is pointing at
# which is also the same object the 'first' key in dictionary references, ergo
# the change is reflected there as well when the dictionary is printed.