# q1; 2 diff ways to remove all elements from given list
'''
numbers = [1, 2, 3, 4]
numbers2 = list(numbers)

print(f'before: {numbers}')
numbers.clear()
print(f'after: {numbers}')

print(f'before: {numbers2}')
del numbers2[:]
print(f'after: {numbers2}')
'''
# solution also has while loop w/ pop() & reassign numbers to empty list w/ caveat
# that og list isn't technically cleared but that's ok if no other refs to it exist

# q2; what will following code output?
'''
print([1, 2, 3] + [4, 5])
'''
# should print [1, 2, 3, 4, 5]; evals expression first which concatenates the two lists

# q3; what will following code output?
'''
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
'''
# prints "hello there"; str immutable so reassign just points it at diff strs, no mutation

# q4; what will following code output?
'''
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
'''
# prints [{"first": 42}, {"second": "value2"}, 3, 4, 5]
# my_list2 points to diff obj than my_list1, but b/c shallow copy, nested refs are same

# q5; rewrite given function so only 1 return that doesn't explicitly use True or False
'''
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
def is_color_valid2(color):
    # return color == "blue" or color == "green"
    return color in ["blue", "green"]
'''