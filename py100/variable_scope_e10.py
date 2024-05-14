# what's my value (part 10)
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# prints [10, 2, 3]; my_function's accessing b directly via lexical scoping
# & b is a mutable type (list) so changes reflect in all vars pointing to it