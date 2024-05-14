def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# error, since second has a default, all subsequent params must also & third doesn't