# q3; given the following similar sets of code, what will each one print
# set A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# outputs 'one is: ["one"]', 'two is ["two"]' and 'three is: ["three"]' b/c
# the identifiers one, two and three inside mess_with_vars() are local variables
# initialized w/ the value/refs of outer scope one, two and three passed in as args,
# but they're ultimately separate entities and therefore their reassignment doesn't
# affect the outer scope variables one, two and three.

# set B
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# outputs the same thing as set A. global keyword wasn't used so again, the one, two
# and three inside mess_with_vars() are local variables that happen to share the same
# name as outer scope variables b/c the params were named thusly; they are in fact
# still separate entities however, so the reassignment doesn't affect outer scope

# set C
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# ok this time, outputs 'one is: ["two"]', 'two is: ["three"]', and 'three is: ["one"]'
# b/c local one, two & three inside mess_with_vars() are initialized w/ references to
# the same list objs their outer scope counterparts are pointing during function invocation,
# when the outer scope vars are passed in as args. therefore when the local variables reassign
# the first element of the list they're pointing at, the mutation is universal for all vars
# pointing to that object, i.e. outer scope one, two and three also reflect the change