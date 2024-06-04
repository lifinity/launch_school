def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# prints 42, 3, 2 on separate lines; both 2nd & 3rd params set as their default args