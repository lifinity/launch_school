# what's my value? (part 5)
a = 1

def my_function():
    print(a)
    a = 2

my_function()

# error b/c presence of a = 2 assignmen means python assumes 
# a is a local variable so can't reference b4 initialization