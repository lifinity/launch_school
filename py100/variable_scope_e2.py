# what's my value? (part 2)
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# raises an error b/c assignment makes python think x is local var
# but when it tries to access x as part of x + 5, can't find init