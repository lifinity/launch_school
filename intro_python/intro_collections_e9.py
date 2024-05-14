my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal?
# yes. my_list == another_list would be True; when compared, same elements

# Are the lists assigned to my_list and another_list the same object?
# no they're not the same object; do not share a reference. list constructor creates new obj

# Are the nested lists at index 3 of my_list and another_list equal?
# yes. my_list[3] == another_list[3] is True; when compared, same elements 

# Are the nested lists at index 3 of my_list and another_list the same object?
# yep, same object. list(my_list) creates a shallow copy so reference to my_list[3] copied over
