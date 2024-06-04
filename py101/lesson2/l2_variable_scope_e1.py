num = 5

def my_func():
    print(num)

my_func()

# prints 5; no local num defined so successfully 
# searches for & accesses outer scope (global) var num