foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# prints 'bar' because shadowing only relevant inside function set_foo()