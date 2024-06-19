# multiples of 3 & 5
# write function that computes sum of all num btwn 1 & range_end, inclusive
# that are multiples of 3 or 5, e.g. for range_end = 20, result is 98

def multisum(range_end):
    sum = 0
    for num in range(1, range_end+1):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)