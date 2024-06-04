# three-way comparison
def compare_by_length(str1, str2):
    diff = len(str1) - len(str2)
    return 0 if not diff else (-1 if diff < 0 else 1)
    
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0
