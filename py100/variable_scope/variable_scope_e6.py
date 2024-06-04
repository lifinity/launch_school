# what's my value? (part 6)
a = 1

def my_function():
    a = 2

my_function()
print(a)

# prints 1 b/c a = 2 inside my_function initializes a new separate local var a
# that has no impact on global a & can't be accessed from outside function scope