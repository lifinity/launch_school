def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# prints 42, 3.141592, 2 on separate lines; 3rd param defaults to 2