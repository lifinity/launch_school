# odd numbers
# print all odd #s from 1 - 99 inclusive w/ each num on separate line
# bonus: solve problem by iterating over just odd #s

'''
for odd_num in range(1, 100, 2):
    print(odd_num)
'''

# further exploration: let user specify start & end range (inclusive)
# interpreted this as being able to pass in start/end via function args
# but could code this to directly receive user input via input() too
def display_odds(start, end):
    adjusted_start = start if start % 2 else start + 1
    for odd_num in range(adjusted_start, end+1, 2):
        print(odd_num)

display_odds(1, 99)