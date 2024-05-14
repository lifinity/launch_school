numbers1 = [1, 3, 5, 7, 9, 11]    # True
numbers2 = []                     # False
numbers3 = [2, 4, 6, 8]           # False
numbers4 = ['1', '3', '5']        # False 
numbers5 = ['1', 3.0, '5']        # True

print(3 in numbers1) 
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)
