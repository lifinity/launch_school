num = 5

def my_func():
    num = 10

my_func()
print(num)

# prints 5 b/c the num initialized on line 4 is
# local to & shadows the global num inside my_func
# but is a separate entity from the outer scope num
# i.e. doesn't & can't reassign it to be 10