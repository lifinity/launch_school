# running totals
# write a function that takes a list of numbers & returns a list w/ same
# num of elements, but each element's val being running total from og list

# input: list of numbers (ints? assumed)
# output: list of numbers (running totals)

# explicit rules
# - input list & output list should have same length
# - the val @ each idx of the output list should be the sum of the vals of
# all idx prior to it from input list + the val @ that idx in the input list

# implicit rules
# - empty list as input should return empty list as output

# questions (theoretical)
# - any limits around max input length or max element magnitude?
# - positive numbers only? & just ints or floats ok as well?
# - expect only valid input, or account for non-numerical elements?

# data structures
# list, since that's the output & need to apply a transformation

# algorithm
# 1. for each num in input list, sum up all prev num up to and including current 
# 2. save that sum into a list and return @ loop end

# implementation options
# can use sum() on slice OR get prev val & add current OR counter w/ running total

def running_total(nums):
    return [sum(nums[:idx+1]) for idx in range(len(nums))]

def running_total_alt(nums):
    totals = []
    for idx, num in enumerate(nums):
        totals.append(num if not totals else totals[idx-1] + num)
    return totals

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True