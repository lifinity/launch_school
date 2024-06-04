# q1; will this raise an error?
'''
numbers = [1, 2, 3]
numbers[6] = 5
'''
# yeah, IndexError; trying to access element beyond len of list.

# q2; write code to determine if given str ends in exclamation mark?
'''
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def str_ends_in(_str, substr):
    return bool(_str[-1] == substr)

print(f"'{str1}' ends in '!'? {str_ends_in(str1, '!')}")
print(f"'{str2}' ends in '!'? {str_ends_in(str2, '!')}")
'''
# actual solution was to use str1.endswith('!')

# q3; given str, 2 diff ways to make new str w/ 'Four score and ' prepended
'''
famous_words = "seven years ago..."
prefix = 'Four score and '

print(prefix + famous_words)
print(f'{prefix}{famous_words}')
print(''.join([prefix, famous_words]))
'''

# q4; given str, print str w/ same val but all lowercase except first letter caps
'''
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

print(munsters_description.capitalize())
'''

# q5; given str, print w/ case of all letters swapped
'''
munsters_description = "The Munsters are creepy and spooky."
# ==> "tHE mUNSTERS ARE CREEPY AND SPOOKY."

print(munsters_description.swapcase())
'''

# q6; determine if name 'Dino' appears in given strs, check separately
'''
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print('Dino' in str1) # False, case-sensitive
print('Dino' in str2) # True
'''

# q7; how can we add family pet 'Dino' to given list?
'''
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.append('Dino')
print(flintstones)
'''

# q8; add multiple items to given list using another method instead of append?
'''
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.extend(['Dino', 'Hoppy'])
print(flintstones)
'''

# q9; print new version of given str that ends just before word 'house'
'''
advice = "Few things in life are as important as house training your pet dinosaur."
# ==> 'Few things in life are as important as'

print(advice[:advice.find('house')])
'''
# actual solution used advice.split("house")[0]

# q10; print given str w/ word 'important' replaced by 'urgent'
'''
advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.replace('important', 'urgent'))
'''