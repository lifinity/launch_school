# what century is that?
# write a function that takes a yr as input & returns the century; return val should
# be a string that begins w/ the century # & ends w/ st, nd, rd or th as appropriate
# new centuries begin in yrs ending w/ 01, e.g. 1901-2000 is the 20th century

# 0th, 1st, 2nd, 3rd, 4th, ... 10th, 11th, 12th, 13th ... 20th, 21st, 22nd, 23rd, ...
def num_suffix(num):
    last_digit = num % 10
    penult_digit = (num // 10) % 10

    if penult_digit == 1:
        return 'th'
    
    match last_digit:
        case 1: return 'st'
        case 2: return 'nd'
        case 3: return 'rd'
        case _: return 'th'

''' 
for num in range(111):
    print(f'{num}{num_suffix(num)}')
'''

# 01-100 = 1st, 101-200 = 2nd, 201-300 = 3rd ... 2001-2100 = 21st
# 5 // 100 = 0 (+1) = 1st
# 100 // 100 = 1 (+0) = 1st <-- special case
# 2101 // 100 = 21 (+1) = 22nd
def century(year):
    century = (year // 100) if year % 100 == 0 else (year // 100) + 1
    return f'{century}{num_suffix(century)}'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True