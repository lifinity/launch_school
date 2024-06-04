# what's my value (part 7)
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# prints 2 b/c using global a so a = 2 reassigns global a to 2