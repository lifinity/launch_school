# what's my value? (part 9)
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# prints 7 b/c changes to params only relevant inside the function
# for which they're defined (except mutable objs); local var b init
# val of arg a which is an int i.e. immutable; separate from global a