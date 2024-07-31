def is_consonant(chr):
    # this function is english-specific/not internationalized
    return chr.casefold() not in 'aeiou' \
       and chr.isalpha()

def count_max_adjacent_consonants(str_):
    spaceless_str = str_.replace(' ', '')
    max_count = 0
    current_count = 0
    for chr in spaceless_str:
        if is_consonant(chr):
            current_count += 1
        else: # is vowel or non-alphabetical character
            if current_count > 1 and max_count < current_count:
                max_count = current_count
            current_count = 0
    return max(max_count, current_count)

print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjecc')) # 4
print('-' * 10)
print(count_max_adjacent_consonants('alt nation'))  # 3
print(count_max_adjacent_consonants(''))            # 0
print(count_max_adjacent_consonants('      '))      # 0
print(count_max_adjacent_consonants(' tm r  ro w')) # 4
print(count_max_adjacent_consonants('kkkkk'))       # 5  

def sort_by_consonant_count(str_list):
    sorted = str_list.copy()
    sorted.sort(key=count_max_adjacent_consonants, reverse=True)
    return sorted

print('-' * 10)
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']