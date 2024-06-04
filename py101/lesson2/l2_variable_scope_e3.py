num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# prints 10 because global keyword indicates
# to use global variable num inside my_func
# therefore the reassignment is on line 5 is
# happening to the same num that lives in the outer scope