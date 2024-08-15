# given following code, what are final vals of a & b? answer w/o running

a = 2
b = [5, 8]
lst = [a, b]    # [2, [5, 8]]

lst[0] += 2     # [4, [5, 8]]
lst[1][0] -= a  # [4, [3, 8]]

# final val of a is 2 b/c ints immutable & a never reassigned to point away
# from immutable val of 2. final val of b is [3, 8] b/c 1st element (5) of
# list obj it was pointing to was mutated via subtracting val of var a (2)
# from it to produce an updated val of 3.

print(a)
print(b)
print(lst)