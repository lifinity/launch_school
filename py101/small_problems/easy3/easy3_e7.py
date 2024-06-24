# double doubles
# double # is even-length # whose left side digits are same as right-side, e.g. 103103
# write function that takes a number as an arg & return it multiplied by 2, unless arg
# is double number, in which case return as-is

# whether # is negative seems to be irrelevant; only care that digits are same
def is_double(num):
    num_str = str(abs(num))
    mid = len(num_str) // 2
    return num_str[:mid] == num_str[mid:]

print(is_double(0) == False)
print(is_double(444) == False)
print(is_double(3333) == True)
print(is_double(12711271) == True)
print(is_double(1235123) == False)
print(is_double(-828828) == True)

print("-" * 30)

def twice(num):
    return num if is_double(num) else num * 2
    
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True