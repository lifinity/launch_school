def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# prints 'Inner 1: 25' when inner_func1() invoked b/c
# new local var x initialized w/ value of 25, then prints
# 'Inner 2: 15' b/c inner_func2() invoked but doesn't
# define its own local var x so accesses outer scope x
# defined in parent my_func() which still has val of 15
# b/c its separate from the local one initialized inside inner_func1()