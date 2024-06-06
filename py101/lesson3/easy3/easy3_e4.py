# q4; what will following code output?
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# prints [{"first": 42}, {"second": "value2"}, 3, 4, 5]
# my_list2 points to diff obj than my_list1, but b/c shallow copy, nested refs are same