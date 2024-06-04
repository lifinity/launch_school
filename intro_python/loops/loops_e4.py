my_list = [6, 3, 0, 11, 20, 4, 17]

print('WHILE LOOP:')    # even numbers
idx = 0
while idx < len(my_list):
    val = my_list[idx]
    if val % 2 == 0:
        print(val)
    idx += 1

print('FOR LOOP:')      # odd numbers
for num in [e for e in my_list if e % 2]:
    print(num)
